# graph.py
import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.messages import SystemMessage, HumanMessage
from datetime import datetime
from langchain_tavily import TavilySearch
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from .helper import Context, save_output, call_llm, build_context_str, build_search_queries, run_tavily, format_tavily_results













# ── Nodes ─────────────────────────────────────────────────────────────────────

def outline_node(state: Context) -> dict:
    result = call_llm("outline.md", build_context_str(state))
    return {"outline": result}

def search_node(state: Context) -> dict:
    queries        = build_search_queries(state["topic"], state["content_type"])
    results        = run_tavily(queries)
    tavily_context = format_tavily_results(results)

    user_content = (
        f"{build_context_str(state)}\n\n"
        f"TAVILY SEARCH RESULTS:\n"
        f"{tavily_context}"
    )

    result = call_llm("search.md", user_content)
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
 
    
