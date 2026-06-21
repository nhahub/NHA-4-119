# graph.py
import json
import os
import re
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.messages import SystemMessage, HumanMessage
from datetime import datetime

from json_repair import repair_json
from langchain_openrouter import ChatOpenRouter





# ── State ─────────────────────────────────────────────────────────────────────



class Context(TypedDict):
    job_id: str
    topic: str
    audience: str | None
    tone: str
    content_type: str
    brief: str | None
    reference_text: str | None
    outline: dict
    search: dict
    active_writer: str
    draft: dict
    critique: dict
    revision_count: int
    final_content: str

# ── LLM ───────────────────────────────────────────────────────────────────────

api_key=""
llm = ChatOpenRouter(
    model="meta-llama/llama-3.1-8b-instruct",
    api_key=api_key,
    
)


# ── Helpers ───────────────────────────────────────────────────────────────────

# Get the directory where graph.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level to src/, then into prompts/
PROMPTS_DIR = os.path.join(BASE_DIR, "..", "prompts")

def save_output(result: Context, content_type: str):
    """Save the full pipeline output to a JSON file."""
    
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "outputs")
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{content_type}_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    # Build a clean output dict — only the useful fields
    output = {
        "meta": {
            "job_id":       result.get("job_id"),
            "topic":        result.get("topic"),
            "audience":     result.get("audience"),
            "tone":         result.get("tone"),
            "content_type": result.get("content_type"),
            "timestamp":    timestamp,
        },
        "outline":        result.get("outline", {}),
        "search":         result.get("search", {}),
        "draft":          result.get("draft", {}),
        "critique": {
            "scores":        result.get("critique", {}).get("scores"),
            "overall_score": result.get("critique", {}).get("overall_score"),
            "status":        result.get("critique", {}).get("status"),
            "passed_elements": result.get("critique", {}).get("passed_elements"),
            "warnings":      result.get("critique", {}).get("warnings"),
        },
        "revision_count": result.get("revision_count"),
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"💾 Output saved to: {filepath}")
    return filepath


def load_prompt(filename: str) -> str:
    path = os.path.join(PROMPTS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def fix_json_string(raw: str) -> str:
    """
    Fix unescaped newlines and control characters inside JSON string values.
    Only escapes characters that appear inside quoted strings.
    """
    result = []
    in_string = False
    escape_next = False

    for char in raw:
        if escape_next:
            result.append(char)
            escape_next = False
            continue

        if char == '\\' and in_string:
            escape_next = True
            result.append(char)
            continue

        if char == '"':
            in_string = not in_string
            result.append(char)
            continue

        if in_string and char == '\n':
            result.append('\\n')
            continue

        if in_string and char == '\r':
            result.append('\\r')
            continue

        if in_string and char == '\t':
            result.append('\\t')
            continue

        result.append(char)

    return ''.join(result)


def call_llm(prompt_file: str, user_content: str) -> dict:
    messages = [
        SystemMessage(content=load_prompt(prompt_file)),
        HumanMessage(content=user_content),
    ]
    response = llm.invoke(messages)
    raw = response.content

    if not raw or not raw.strip():
        raise ValueError(f"[{prompt_file}] LLM returned empty response.")

    # Extract JSON block if wrapped in fences or prose
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
    if match:
        cleaned = match.group(1).strip()
    else:
        match = re.search(r"\{[\s\S]*\}", raw)
        cleaned = match.group(0).strip() if match else raw.strip()

    # Repair and parse — handles missing commas, unclosed brackets,
    # unescaped newlines, trailing text, and most LLM JSON mistakes
    repaired = repair_json(cleaned)
    return json.loads(repaired)
def build_context_str(state: Context) -> str:
    """Serialize relevant state fields as JSON for the LLM."""
    return json.dumps({
        "topic":          state["topic"],
        "audience":       state["audience"],
        "tone":           state["tone"],
        "content_type":   state["content_type"],
        "brief":          state.get("brief"),
        "reference_text": state.get("reference_text"),
        "outline":        state.get("outline", {}),
        "search":         state.get("search", {}),
        "draft":          state.get("draft", {}),
        "critique":       state.get("critique", {}),
        "revision_count": state.get("revision_count", 0),
    })

# ── Nodes ─────────────────────────────────────────────────────────────────────

def outline_node(state: Context) -> dict:
    result = call_llm("outline.md", build_context_str(state))
    return {"outline": result}

def search_node(state: Context) -> dict:
    result = call_llm("search.md", build_context_str(state))
    return {"search": result}

def router_node(state: Context) -> dict:
    writer_map = {
        "blog":        "blog_writer",
        "linkedin":    "linkedin_writer",
        "tweet":       "tweet_writer",
        "instagram":   "instagram_writer",
        "short_story": "story_writer",
    }
    active = writer_map.get(state["content_type"])
    if not active:
        raise ValueError(f"Unknown content_type: {state['content_type']}")
    return {"active_writer": active}

def blog_writer_node(state: Context) -> dict:
    result = call_llm("blog_writer.md", build_context_str(state))
    return {"draft": result}

def linkedin_writer_node(state: Context) -> dict:
    result = call_llm("linkedin_writer.md", build_context_str(state))
    return {"draft": result}

def tweet_writer_node(state: Context) -> dict:
    result = call_llm("tweet_writer.md", build_context_str(state))
    return {"draft": result}

def instagram_writer_node(state: Context) -> dict:
    result = call_llm("instagram_writer.md", build_context_str(state))
    return {"draft": result}

def story_writer_node(state: Context) -> dict:
    result = call_llm("story_writer.md", build_context_str(state))
    return {"draft": result}

def critique_node(state: Context) -> dict:
    result = call_llm("critique.md", build_context_str(state))
    return {
        "critique":       result,
        "revision_count": state.get("revision_count", 0) + 1,
    }

# ── Conditional Edges ─────────────────────────────────────────────────────────

def dispatch_writer(state: Context) -> str:
    """Routes from router node to the correct writer node."""
    return state["active_writer"]

def critique_edge(state: Context) -> str:
    """After critique: loop back to writer or end."""
    status = state["critique"].get("status")
    if status == "PASS" or state["revision_count"] >= 3:
        return END
    return state["active_writer"]  # loop back to same writer

# ── Graph ─────────────────────────────────────────────────────────────────────

def build_graph() -> StateGraph:
    graph = StateGraph(Context)

    # Register nodes
    graph.add_node("outline",          outline_node)
    graph.add_node("search",           search_node)
    graph.add_node("router",           router_node)
    graph.add_node("blog_writer",      blog_writer_node)
    graph.add_node("linkedin_writer",  linkedin_writer_node)
    graph.add_node("tweet_writer",     tweet_writer_node)
    graph.add_node("instagram_writer", instagram_writer_node)
    graph.add_node("story_writer",     story_writer_node)
    graph.add_node("critique",         critique_node)

    # Entry → parallel upstream agents
    graph.set_entry_point("outline")
    graph.add_edge("outline", "search")
    graph.add_edge("search",  "router")

    # Router → correct writer
    graph.add_conditional_edges(
        "router",
        dispatch_writer,
        {
            "blog_writer":      "blog_writer",
            "linkedin_writer":  "linkedin_writer",
            "tweet_writer":     "tweet_writer",
            "instagram_writer": "instagram_writer",
            "story_writer":     "story_writer",
        }
    )

    # All writers → critique
    for writer in ["blog_writer", "linkedin_writer", "tweet_writer",
                   "instagram_writer", "story_writer"]:
        graph.add_edge(writer, "critique")

    # Critique → loop or end
    graph.add_conditional_edges(
        "critique",
        critique_edge,
        {
            "blog_writer":      "blog_writer",
            "linkedin_writer":  "linkedin_writer",
            "tweet_writer":     "tweet_writer",
            "instagram_writer": "instagram_writer",
            "story_writer":     "story_writer",
            END:                END,
        }
    )

    return graph.compile()

#app = build_graph()

def run_test(app, content_type: str):
    """Run a mock pipeline job for a given content_type."""
    print(f"\n{'='*60}")
    print(f"TEST: content_type = '{content_type}'")
    print("="*60)
 
    initial_state: Context = {
        "job_id":         "test-001",
        "topic":          "The Future of AI in Content Creation",
        "audience":       "Marketing professionals",
        "tone":           "professional",
        "content_type":   content_type,
        "brief":          None,
        "reference_text": None,
        "outline":        {},
        "search":         {},
        "active_writer":  "",
        "draft":          {},
        "critique":       {},
        "revision_count": 0,
        "final_content":  "",
    }
 
    result = app.invoke(initial_state)
     # Save output
    
    print(f"\n✅ Pipeline complete.")
    print(f"   Active writer : {result['active_writer']}")
    print(f"   Critique status: {result['critique'].get('status')}")
    print(f"   Overall score  : {result['critique'].get('overall_score')}")
    print(f"   Revision count : {result['revision_count']}")
    save_output(result, content_type)
    return result


 #── Main ───────────────────────────────────────────────────────────────────────
 
if __name__ == "__main__":
    print("Building Lexium graph...")
    app = build_graph()
 
    
 
    # Test each content type
    for content_type in ["blog", "linkedin", "tweet", "instagram", "short_story"]:
        run_test(app, content_type)
 
    print("\n🎉 All tests passed.")
 
    