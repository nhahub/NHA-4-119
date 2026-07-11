# 🚀 LEXORA — Agentic AI Content Generation Platform

An end-to-end **DEPI project** for building an AI-powered content generation platform using a modern **React frontend**, **FastAPI backend**, and a structured **multi-agent AI workflow**.

LEXORA transforms a user’s idea into polished, ready-to-use English content for different platforms and writing scenarios.

---

## 📌 Overview

This repository contains the complete implementation of **LEXORA**, an agentic AI content generation platform developed as part of the **Digital Egypt Pioneers Initiative — DEPI**.

The system allows users to enter a topic, select a content type, choose a writing tone, and optionally provide more context such as:

- Target audience
- Writing brief
- Reference text
- Maximum output size

The request is sent from the React frontend to the FastAPI backend.

The backend creates a generation job and processes it through a structured AI workflow that includes planning, research, routing, writing, reviewing, and revising the generated content.

LEXORA currently supports:

- 📝 Blog Posts
- 💼 LinkedIn Posts
- 🐦 Tweets
- 📸 Instagram Captions
- 📖 Short Stories

The current system generates content in **English only**.

---

## 🎯 Project Objectives

The main objectives of LEXORA are to:

- Build a complete end-to-end AI content generation platform
- Generate different types of professional and creative content
- Apply an agent-based AI workflow instead of using a single direct prompt
- Connect a modern frontend to a production-style backend API
- Integrate language models through OpenRouter
- Use Tavily for external research and supporting context
- Track generation jobs asynchronously
- Support PostgreSQL database storage
- Provide a clean and responsive user interface
- Demonstrate a practical Agentic AI system for the DEPI project

---

## ✨ Main Features

LEXORA provides the following features:

- Generate five different content formats
- Select a writing tone
- Specify the target audience
- Add custom instructions or a writing brief
- Add reference text
- Select the preferred output size
- Track generation job progress
- Display the current generation status
- Copy generated content
- Download generated content as a text file
- Responsive user interface
- Job-based FastAPI backend
- Multi-agent AI workflow
- OpenRouter language model integration
- Tavily search integration
- PostgreSQL database support
- In-memory storage fallback

---

## 📝 Supported Content Types

| Content Type | Backend Value | Description |
|---|---|---|
| Blog Post | `blog` | Structured long-form content with clear sections and a strong conclusion |
| LinkedIn Post | `linkedin` | Professional social content with a hook, useful value, and call to action |
| Tweet | `tweet` | Short-form content suitable for quick social publishing |
| Instagram Caption | `instagram` | Engaging captions with a natural social style and optional hashtags |
| Short Story | `short_story` | Creative narrative content with characters, atmosphere, and story flow |

---

## 🎭 Supported Tones

The backend currently supports the following writing tones:

- Professional
- Casual
- Witty
- Inspirational
- Educational
- Neutral

The frontend also provides a `None` option.

When the user selects `None`, the frontend does not send a tone value, and the backend uses its default tone.

---

## 🧠 Agent Workflow

LEXORA uses a structured multi-agent workflow to improve the quality of the generated content.

### 1️⃣ Outline Agent

The Outline Agent analyzes the user request and creates an initial structure for the required content.

It identifies:

- The main idea
- Important sections
- Content direction
- Suggested writing structure

---

### 2️⃣ Search Agent

The Search Agent uses **Tavily Search** to collect useful information related to the topic.

The research results are used internally to improve the accuracy, context, and usefulness of the generated content.

---

### 3️⃣ Router Agent

The Router Agent selects the correct writing path based on the selected content type.

For example:

- Blog content follows a long-form structure
- LinkedIn content follows a professional social structure
- Tweets follow a short-form structure
- Instagram captions follow a social and engaging structure
- Short stories follow a creative narrative structure

---

### 4️⃣ Writer Agent

The Writer Agent generates the first draft using:

- Topic
- Content type
- Tone
- Target audience
- Brief
- Reference text
- Research context

---

### 5️⃣ Critique Agent

The Critique Agent reviews the generated draft.

It checks areas such as:

- Clarity
- Relevance
- Tone consistency
- Structure
- Content quality
- Platform suitability

---

### 6️⃣ Revision Loop

If the Critique Agent decides that the content needs improvement, the draft is sent back to the Writer Agent.

The Writer Agent then creates an improved version based on the critique.

---

### 7️⃣ Final Result

When the content reaches the required quality, the backend marks the generation job as completed and returns the final content to the frontend.

---

## 🏗️ System Architecture

```text
User
  |
  v
React + Vite Frontend
  |
  v
FastAPI Backend
  |
  v
Generation Job Service
  |
  v
LangGraph Agent Workflow
  |
  +-----------------------------+
  |                             |
  v                             v
OpenRouter Language Model    Tavily Search API
  |                             |
  +-------------+---------------+
                |
                v
       PostgreSQL / Memory Store
                |
                v
        Final Generated Content
```

---

## 🔄 Request Workflow

The complete request flow works as follows:

```text
1. The user enters the generation details
2. The frontend validates the required fields
3. The frontend sends a POST request to FastAPI
4. The backend creates a generation job
5. The backend returns a job ID
6. The frontend polls the job status endpoint
7. The AI agents process the request
8. The backend marks the job as completed
9. The frontend requests the final result
10. The generated content appears on the website
```

---

## ⚙️ Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python 3.11+ |
| Frontend | React, Vite, JavaScript |
| Frontend Styling | CSS |
| Backend API | FastAPI |
| Backend Server | Uvicorn |
| Agent Orchestration | LangGraph |
| Language Model Provider | OpenRouter |
| Search Provider | Tavily |
| Database | PostgreSQL / Neon |
| Database Migrations | Alembic |
| Data Validation | Pydantic |
| Environment Management | Python Dotenv |
| Testing | Pytest |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |

---

## 🗂️ Repository Structure

```text
NHA-4-119/
│
├── src/
│   ├── agents/
│   │   ├── graph.py
│   │   └── helper.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── services/
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── database/
│   ├── models/
│   └── prompts/
│
├── lexora-frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── brand/
│   │   │   ├── common/
│   │   │   └── generator/
│   │   │
│   │   ├── constants/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   └── utils/
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── .env.example
│
├── alembic/
├── data/
├── docs/
├── mlflow/
├── notebooks/
├── tests/
│
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🌐 API Workflow

The frontend does not wait for the complete AI response inside a single HTTP request.

The backend uses an asynchronous job-based workflow.

---

### 📤 Create a Generation Job

```http
POST /api/v1/generate
```

Example request:

```json
{
  "topic": "Benefits of learning artificial intelligence",
  "content_type": "linkedin",
  "tone": "professional",
  "audience": "University students",
  "brief": "Make the post practical and motivational",
  "reference_text": "",
  "max_tokens": 500
}
```

Example response:

```json
{
  "job_id": "example-job-id",
  "status": "queued",
  "message": "Generation job created successfully"
}
```

---

### 🔍 Check Job Status

```http
GET /api/v1/jobs/{job_id}
```

Example response:

```json
{
  "job_id": "example-job-id",
  "status": "running",
  "progress": 30,
  "message": "Running outline, research, writer, and critique agents",
  "error": null
}
```

---

### 📄 Get Final Result

```http
GET /api/v1/jobs/{job_id}/result
```

The frontend continues checking the job status until the job becomes:

```text
completed
```

or:

```text
failed
```

---

## 🔌 Main API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Display basic API information |
| GET | `/health` | Check backend health status |
| POST | `/api/v1/generate` | Create a new generation job |
| GET | `/api/v1/jobs/{job_id}` | Get the current job status |
| GET | `/api/v1/jobs/{job_id}/result` | Get the completed generated content |
| GET | `/api/v1/jobs/{job_id}/debug` | Get backend debugging details |

The debug endpoint is available for backend development and troubleshooting.

Debug details are not displayed in the user interface.

---

## 🔐 Environment Configuration

The project uses separate environment files for the backend and frontend.

---

## 🖥️ Backend Environment File

Create a file named:

```text
.env
```

in the main project directory:

```text
NHA-4-119/.env
```

Example:

```env
# ==========================================
# AI Providers
# ==========================================

OpenRouter_API_KEY=your_openrouter_key_here
TAVILY_API_KEY=your_tavily_key_here


# ==========================================
# Database
# ==========================================

DATABASE_URL=your_postgresql_database_url_here
JOB_STORE_STRICT_DATABASE=false


# ==========================================
# Application
# ==========================================

APP_NAME=LEXORA Content Generation API
DEBUG=false
LOG_LEVEL=INFO


# ==========================================
# CORS
# ==========================================

CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:5174,http://127.0.0.1:5174


# ==========================================
# Model Configuration
# ==========================================

MODEL_PATH=
MODEL_NAME=meta-llama/llama-3.1-8b-instruct
MAX_TOKENS=500
TEMPERATURE=0.7
TOP_P=0.9


# ==========================================
# Server
# ==========================================

HOST=0.0.0.0
PORT=8000
```

The real `.env` file must not be uploaded to GitHub.

The `.env.example` file should contain placeholder values only.

---

## 🎨 Frontend Environment File

Create a file named:

```text
.env
```

inside:

```text
lexora-frontend/
```

Add:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

This value tells the frontend where the FastAPI backend is running.

---

## 💻 Local Installation

Before running the project, make sure the following software is installed:

- Python 3.11 or newer
- Node.js LTS
- npm
- Git

---

## ▶️ Running the Backend

Open Command Prompt and navigate to the main project directory:

```cmd
cd /d "D:\DEPI project\NHA-4-119"
```

Create a Python virtual environment:

```cmd
python -m venv .venv
```

Activate the virtual environment:

```cmd
.venv\Scripts\activate
```

After activation, the terminal should look similar to:

```text
(.venv) D:\DEPI project\NHA-4-119>
```

Upgrade pip:

```cmd
python -m pip install --upgrade pip
```

Install the backend dependencies:

```cmd
python -m pip install -r requirements.txt --index-url https://pypi.org/simple
```

Run the FastAPI backend:

```cmd
python -m uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

---

## ❤️ Backend Health Check

Open:

```text
http://127.0.0.1:8000/health
```

A successful response should look similar to:

```json
{
  "status": "ok",
  "model_loaded": true,
  "uptime_seconds": 120
}
```

---

## 📚 Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to view and test the backend endpoints.

Keep the backend terminal open while using the application.

---

## ▶️ Running the Frontend

Open a second Command Prompt window:

```cmd
cd /d "D:\DEPI project\NHA-4-119\lexora-frontend"
```

Install the frontend dependencies:

```cmd
npm install --registry=https://registry.npmjs.org/
```

This command is only required the first time or after changing dependencies.

Run the frontend:

```cmd
npm run dev
```

Vite will display a local URL such as:

```text
http://localhost:5173
```

If Port `5173` is already in use, Vite may use:

```text
http://localhost:5174
```

Make sure the frontend port is included in the backend `CORS_ORIGINS` value.

---

## 🔄 Running the Complete System

The frontend and backend must run at the same time.

```text
Terminal 1
FastAPI Backend
http://127.0.0.1:8000
```

```text
Terminal 2
React Frontend
http://localhost:5173
```

or:

```text
http://localhost:5174
```

The complete system flow is:

```text
Frontend
   |
   v
FastAPI Backend
   |
   v
Generation Job
   |
   v
OpenRouter + Tavily
   |
   v
Multi-Agent Workflow
   |
   v
Final Generated Content
```

---

## 🧪 Example Generation Request

Example user input:

```text
Topic: Benefits of learning artificial intelligence

Content Type: LinkedIn Post

Tone: Professional

Audience: University students

Brief: Make the post practical and motivational
```

The backend creates a job, executes the multi-agent workflow, and sends the final generated content to the frontend.

---

## 🧪 Testing OpenRouter

Navigate to the project directory and activate the backend environment:

```cmd
cd /d "D:\DEPI project\NHA-4-119"
.venv\Scripts\activate
```

Run:

```cmd
python -c "from src.agents.helper import get_llm; print(get_llm().invoke('Reply with only the word OK').content)"
```

A successful response should be:

```text
OK
```

---

## 🔎 Testing Tavily

Run:

```cmd
python -c "from src.agents.helper import get_tavily; result=get_tavily().invoke({'query':'artificial intelligence'}); print(str(result)[:1000])"
```

A successful response should contain search results.

---

## 🧪 Testing the Application

To test the complete application:

1. Start the FastAPI backend
2. Open the `/health` endpoint
3. Start the React frontend
4. Open the Generate page
5. Enter a topic
6. Select a content type
7. Select a tone
8. Press **Generate Content**
9. Wait for the job to complete
10. Review the final generated result
11. Test Copy
12. Test Download

---

## 📊 Generation Job Status

A generation job may have one of the following states:

| Status | Meaning |
|---|---|
| `idle` | No generation job has started |
| `queued` | The request has been accepted |
| `running` | The agent workflow is processing the request |
| `completed` | The final content has been generated successfully |
| `failed` | The generation process failed |

---

## 🛡️ Security Notes

- Never upload the real `.env` file to GitHub
- Never include real API keys inside `.env.example`
- Never share screenshots containing API keys
- Revoke exposed OpenRouter keys immediately
- Revoke exposed Tavily keys immediately
- Change exposed database credentials
- Do not connect the React frontend directly to OpenRouter
- AI provider requests must pass through the FastAPI backend
- Do not expose backend debugging information to normal users
- Add authentication and rate limiting before production deployment

Correct architecture:

```text
Frontend → FastAPI Backend → OpenRouter / Tavily
```

Incorrect architecture:

```text
Frontend → OpenRouter
```

---

## 📌 Current Project Scope

The current version includes:

- React web frontend
- FastAPI backend
- Multi-agent generation workflow
- Five content formats
- Tone selection
- Target audience input
- Writing brief input
- Reference text input
- Output size selection
- Job progress tracking
- Copy functionality
- Text file download
- PostgreSQL support
- Neon database connection
- In-memory job storage fallback
- OpenRouter integration
- Tavily integration
- Swagger API documentation
- Responsive user interface

---

## 🚫 Out of Scope

The current version does not include:

- Login
- Registration
- User accounts
- User profiles
- Generation history
- Payment system
- Subscription plans
- Admin dashboard
- User-facing debug information
- Production rate limiting
- Live collaboration
- Multiple output languages

---

## ⚠️ Known Limitations

The current version has some limitations:

- Complex generation requests may take several minutes
- The current progress value does not represent every agent separately
- The job may remain at `30%` while the complete workflow is running
- The generated Tweet may sometimes be longer than a single Tweet
- Research source text may occasionally appear inside the final output
- Model settings may require additional backend configuration
- Database migrations may need to be executed before production deployment
- The health endpoint verifies that the application is running but does not fully validate all external providers

---

## 🔮 Future Improvements

Possible future improvements include:

- Improve prompt rules for every content type
- Enforce Tweet character limits
- Add Twitter Thread as a separate content type
- Improve research source cleanup
- Add real per-agent progress tracking
- Add generation history
- Add authentication
- Add role-based access control
- Add rate limiting
- Add retry logic
- Add request timeout handling
- Add automatic provider health checks
- Add model selection
- Add multiple language support
- Add more content types
- Add document export
- Add Markdown export
- Add PDF export
- Add production monitoring
- Add centralized logging
- Improve automated tests
- Improve Docker configuration
- Deploy the frontend and backend to cloud services

---

## 📂 Documentation

The repository may contain documentation related to:

- Project planning
- Project proposal
- Requirements gathering
- System analysis
- System design
- Risk assessment
- Team responsibilities
- Literature review
- Testing reports
- Final presentation preparation

Older documentation should be reviewed to make sure it matches the current LEXORA implementation.

Any documentation related to:

- Product Description Generation
- GPT-2 fine-tuning
- Streamlit
- GAN-based text generation

should be updated or archived because it does not represent the current production workflow.

---

## ✅ Project Status

The current system is operational end-to-end.

Verified components include:

- React frontend startup
- FastAPI backend startup
- Frontend-to-backend connection
- CORS configuration
- Backend health endpoint
- Swagger documentation
- Generation job creation
- Job status polling
- OpenRouter connection
- Tavily connection
- Multi-agent workflow execution
- Final result retrieval
- Final result display
- Copy functionality
- Download functionality

---

## 🏁 Conclusion

LEXORA is a practical and scalable agentic AI content generation platform developed as part of the DEPI project workflow.

The system combines:

- A modern React and Vite frontend
- A FastAPI backend
- OpenRouter language models
- Tavily web search
- LangGraph agent orchestration
- PostgreSQL database support
- A structured generation job workflow

LEXORA demonstrates how modern AI services, backend APIs, agent-based workflows, databases, and frontend technologies can be combined into one complete application.

The project is capable of generating multiple types of English content while providing a clear user experience, asynchronous job processing, content review, revision, and final result delivery.

This repository serves as both a functional AI application and a practical demonstration of end-to-end Agentic AI system development.
