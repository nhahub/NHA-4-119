# LEXIUM — AI Content Generation Platform
## System Architecture v2.0

---

# PART 1: WHAT CHANGED FROM v1

| v1 | v2 |
|---|---|
| Generic `writer.md` + separate format agents | One purpose-built writer per content type |
| Format agents pretended to "shape" mismatched drafts | Each writer owns structure, tone, length, and platform rules |
| `writer.md` removed | Replaced by `router.md` + 5 type-specific writers |
| `blog.md`, `linkedin_post.md`, `tweet.md`, `instagram_post.md`, `short_story.md` removed | Merged into their respective writers |

---

# PART 2: SYSTEM ARCHITECTURE

## Pipeline

```
USER INPUT
  topic, audience, tone, content_type, brief (optional), reference_text (optional)
        │
        ├─────────────────────────┐
        ▼                         ▼
  [outline.md]             [search.md]          ← PARALLEL
  Builds content skeleton   Fetches facts,
  tailored to content_type  citations, keywords
        │                         │
        └──────────┬──────────────┘
                   ▼
            [router.md]                         ← DECISION EDGE
     Reads content_type from LexiumContext.
     Validates upstream outputs are complete.
     Dispatches to exactly one writer.
                   │
       ┌───────────┼───────────┬───────────┬───────────┐
       ▼           ▼           ▼           ▼           ▼
[blog_writer]  [linkedin_  [tweet_     [instagram_ [story_
               writer]     writer]     writer]     writer]
       │           │           │           │           │
       └───────────┴───────────┴───────────┴───────────┘
                   ▼
            [critique.md]                       ← QUALITY GATE
     Scores on 5 dimensions.
     Loops back to active writer if score < 7/10.
     Max 3 iterations, then PASS_WITH_WARNINGS.
                   ▼
            Final plain text output
            delivered to user
```

---

# PART 3: SHARED CONTEXT OBJECT

All agents read from and write to a single `LexiumContext` JSON object:

```json
{
  "job_id": "uuid",
  "topic": "string",
  "audience": "string | null",
  "tone": "professional | casual | witty | inspirational | educational | neutral",
  "content_type": "blog | linkedin | tweet | instagram | short_story",
  "brief": "string | null",
  "reference_text": "string | null",
  "outline": { ... },
  "search": { ... },
  "active_writer": "string (set by router)",
  "draft": { ... },
  "critique": { ... },
  "revision_count": 0,
  "final_content": "string"
}
```

---

# PART 4: AGENT RESPONSIBILITIES

| File | Role | Writes To |
|---|---|---|
| `outline.md` | Builds section skeleton for the selected content type | `context.outline` |
| `search.md` | Fetches verified facts, citations, SEO keywords | `context.search` |
| `router.md` | Validates context, sets active_writer, dispatches | `context.active_writer` |
| `blog_writer.md` | Writes full SEO blog article | `context.draft` |
| `linkedin_writer.md` | Writes LinkedIn thought-leadership post | `context.draft` |
| `tweet_writer.md` | Writes single tweet or thread | `context.draft` |
| `instagram_writer.md` | Writes Instagram caption + hashtag block | `context.draft` |
| `story_writer.md` | Writes short fiction with narrative craft | `context.draft` |
| `critique.md` | Scores draft, loops back or passes | `context.critique` |

---

# PART 5: PROMPT MAINTENANCE GUIDE

## Versioning
Each file carries: `# LEXIUM PROMPT v2.0 | Updated: YYYY-MM-DD | Agent: [name]`

## Adding a New Content Type
1. Create a new `[type]_writer.md` following the same INPUT / TASK / CONSTRAINTS / OUTPUT structure
2. Add the new type to `router.md` dispatch table
3. Add the new type to `outline.md` section flow rules
4. Add keyword logic to `search.md` if SEO is relevant

## Red Lines — Never Change
- ANTI-HALLUCINATION RULE in `search.md`
- REVISION LIMIT (max 3) in `critique.md`
- CONTENT SAFETY block in `story_writer.md`
- JSON key names in all OUTPUT FORMAT blocks (downstream agents depend on exact keys)
- The router's VALIDATION BLOCK — never skip upstream checks
