import json
import os
import re
from typing import TypedDict
from langchain_core.messages import SystemMessage, HumanMessage
from datetime import datetime

from langchain_tavily import TavilySearch
from json_repair import repair_json
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

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

load_dotenv()  # Load environment variables from .env file

_llm: ChatOpenRouter | None = None
_tavily: TavilySearch | None = None


def get_llm() -> ChatOpenRouter:
    """Create the OpenRouter client only when a job actually needs it."""
    global _llm
    if _llm is None:
        api_key = os.getenv("OpenRouter_API_KEY")
        if not api_key:
            raise RuntimeError("OpenRouter_API_KEY is missing from the environment.")

        _llm = ChatOpenRouter(
            model="meta-llama/llama-3.1-8b-instruct",
            api_key=api_key,
        )
    return _llm


def get_tavily() -> TavilySearch:
    """Create the Tavily client lazily so the API can start without search keys."""
    global _tavily
    if _tavily is None:
        if not os.getenv("TAVILY_API_KEY"):
            raise RuntimeError("TAVILY_API_KEY is missing from the environment.")

        _tavily = TavilySearch(
            max_results=6,
            search_depth="advanced",
            topic="general",
            include_answer=False,
            include_raw_content=False,
        )
    return _tavily

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
    response = get_llm().invoke(messages)
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
# ── Search Helpers ────────────────────────────────────────────────────────────

def build_search_queries(topic: str, content_type: str) -> list[str]:
    query_map = {
        "blog": [
            topic,
            f"{topic} statistics 2024 2025 2026",
            f"{topic} research study data",
        ],
        "linkedin": [
            topic,
            f"{topic} industry trends 2026",
            f"{topic} professional insights",
        ],
        "tweet": [
            topic,
            f"{topic} latest news",
            f"{topic} surprising facts",
        ],
        "instagram": [
            topic,
            f"{topic} tips tricks",
            f"{topic} inspiring examples",
        ],
        "short_story": [
            topic,
            f"{topic} real stories examples",
            f"{topic} historical events",
        ],
    }
    return query_map.get(content_type, [topic])


def run_tavily(queries: list[str]) -> list[dict]:
    raw_results = []
    tavily = get_tavily()
    for query in queries:
        result = tavily.invoke({"query": query})
        if isinstance(result, list):
            raw_results.extend(result)
        elif isinstance(result, dict) and "results" in result:
            raw_results.extend(result["results"])

    # Deduplicate by URL
    seen = set()
    unique_results = []
    for r in raw_results:
        url = r.get("url", "")
        if url not in seen:
            seen.add(url)
            unique_results.append(r)

    return unique_results[:6]


def format_tavily_results(results: list[dict]) -> str:
    return "\n\n".join([
        f"Title: {r.get('title', 'Unknown')}\n"
        f"Source: {r.get('url', '').split('/')[2] if r.get('url') else 'Unknown'}\n"
        f"URL: {r.get('url', '')}\n"
        f"Content: {r.get('content', '')}"
        for r in results
    ])
