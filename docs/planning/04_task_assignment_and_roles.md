# 04 — Task Assignment & Roles

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Task Assignment & Roles
**Version:** 1.0

---

## Assumptions

> **[ASSUMPTION]** This document assumes a team of **5 members**. Real team member names have not been provided and are therefore represented as Member 1 through Member 5. Replace these placeholders with actual names before submission.

---

## 1. Team Composition

| Member ID | Name (Placeholder) | Primary Role | Secondary Role |
|-----------|--------------------|-------------|----------------|
| Member 1 | *(Insert Name)* | Project Manager | Documentation Lead |
| Member 2 | *(Insert Name)* | ML Engineer | Evaluation Specialist |
| Member 3 | *(Insert Name)* | Data Engineer | Research Support |
| Member 4 | *(Insert Name)* | Backend & DevOps Engineer | API Developer |
| Member 5 | *(Insert Name)* | Research Lead & UI Developer | Quality Assurance |

---

## 2. Role Descriptions and Responsibilities

### 2.1 Member 1 — Project Manager / Documentation Lead

**Primary Responsibilities:**

- Oversee the overall project schedule and ensure milestones are met on time.
- Coordinate weekly team stand-ups and bi-weekly supervisor meetings.
- Maintain the GitHub project board, issue tracker, and sprint backlog.
- Manage risk register and escalate blockers to the supervisor.
- Ensure consistency across all documentation deliverables.
- Compile and review final submission package.

**Documentation Deliverables Owned:**
- `02_project_proposal.md`
- `03_project_plan.md`
- `04_task_assignment_and_roles.md`
- `05_risk_assessment_and_mitigation_plan.md`
- `06_kpis.md`
- `README.md`

**Tools & Technologies:**
- GitHub Projects / Trello / Notion (project management)
- Markdown (documentation)
- Google Docs / Word (draft collaboration)

---

### 2.2 Member 2 — ML Engineer / Evaluation Specialist

**Primary Responsibilities:**

- Lead all model development activities, from baseline fine-tuning to optimised production model.
- Implement the fine-tuning pipeline using Hugging Face `Trainer` API and PyTorch.
- Set up and maintain the MLflow experiment tracking server.
- Conduct hyperparameter optimisation and record results in MLflow.
- Implement the attention visualisation module.
- Develop the SeqGAN experimental module.
- Perform quantitative model evaluation (Perplexity, BLEU score).

**Technical Deliverables Owned:**
- `src/model/train.py` — Fine-tuning script
- `src/model/evaluate.py` — Evaluation script
- `src/model/attention_viz.py` — Attention visualisation
- `src/model/seqgan.py` — Experimental GAN component
- `notebooks/01_baseline_training.ipynb`
- `notebooks/02_hyperparameter_tuning.ipynb`
- `notebooks/03_evaluation.ipynb`

**Tools & Technologies:**
- Python, PyTorch, Hugging Face Transformers (`gpt2-medium`, `distilgpt2`)
- MLflow (experiment tracking)
- NumPy, scikit-learn (metrics)
- Matplotlib / Seaborn (visualisation)

---

### 2.3 Member 3 — Data Engineer / Research Support

**Primary Responsibilities:**

- Identify, acquire, and document all data sources.
- Implement the full text preprocessing pipeline: cleaning, normalisation, deduplication, and tokenisation.
- Perform Exploratory Data Analysis (EDA) and produce a summary report.
- Design and implement the Hugging Face `datasets`-compatible data loader.
- Prepare train/validation/test splits.
- Support Member 5 with data-related aspects of the literature review.

**Technical Deliverables Owned:**
- `src/data/download_data.py` — Data acquisition script
- `src/data/preprocess.py` — Text cleaning and normalisation
- `src/data/tokenise.py` — Tokenisation and split creation
- `src/data/dataloader.py` — Custom DataLoader
- `notebooks/00_eda.ipynb` — Exploratory Data Analysis notebook

**Tools & Technologies:**
- Python, Pandas, NumPy
- NLTK, spaCy (text processing)
- Hugging Face `datasets` library
- Matplotlib / Wordcloud (EDA visualisation)

---

### 2.4 Member 4 — Backend & DevOps Engineer / API Developer

**Primary Responsibilities:**

- Design and implement the FastAPI REST service including all endpoints, request/response models, and error handling.
- Integrate the fine-tuned GPT-2 Medium model into the API inference pipeline.
- Write unit tests and integration tests for all API endpoints.
- Write the `Dockerfile` and `docker-compose.yml` for containerised deployment.
- (Optional) Configure Apache Airflow DAG for automated pipeline orchestration.
- Manage CI/CD pipeline setup on GitHub Actions (if time permits).
- Deploy to staging environment and validate system behaviour.

**Technical Deliverables Owned:**
- `src/api/main.py` — FastAPI application
- `src/api/models.py` — Pydantic request/response schemas
- `src/api/inference.py` — Model inference wrapper
- `tests/test_api.py` — API unit and integration tests
- `Dockerfile`
- `docker-compose.yml`
- `airflow/dags/pipeline_dag.py` (optional)

**Tools & Technologies:**
- FastAPI, Uvicorn
- Docker, Docker Compose
- GitHub Actions (CI/CD, optional)
- Apache Airflow (optional)
- pytest (testing)

---

### 2.5 Member 5 — Research Lead & UI Developer / Quality Assurance

**Primary Responsibilities:**

- Lead the academic literature review and research synthesis.
- Design and implement the Streamlit web interface for interactive content generation.
- Connect the Streamlit UI to the FastAPI backend.
- Design the human evaluation survey and coordinate evaluators (5–10 participants).
- Compile and analyse human evaluation results.
- Perform final quality assurance review of all documentation for academic language, consistency, and completeness.
- Prepare the final presentation slides.

**Technical Deliverables Owned:**
- `ui/app.py` — Streamlit web application
- `ui/components/` — Streamlit UI components (optional modularisation)
- `notebooks/04_attention_analysis.ipynb` — Research notebook for attention analysis

**Documentation Deliverables Owned:**
- `07_literature_review.md`
- `01_recommended_model_selection.md`
- `08_requirements_gathering.md`
- `09_system_analysis_and_design.md`

**Tools & Technologies:**
- Streamlit
- Python `requests` library (API calls from UI)
- LaTeX / Markdown (academic writing)
- Google Forms / SurveyMonkey (human evaluation)
- PowerPoint / Google Slides (presentation)

---

## 3. Responsibility Matrix (RACI)

> **Legend:** R = Responsible | A = Accountable | C = Consulted | I = Informed

| Task | M1 (PM) | M2 (ML) | M3 (Data) | M4 (DevOps) | M5 (Research/UI) |
|------|---------|---------|-----------|-------------|-----------------|
| Project planning & scheduling | A/R | C | C | C | C |
| Risk & KPI definition | A/R | C | I | I | C |
| Literature review | I | C | C | I | A/R |
| Model selection | C | A/R | I | I | R |
| Data acquisition | I | C | A/R | I | I |
| EDA & preprocessing | I | C | A/R | I | I |
| GPT-2 fine-tuning | I | A/R | C | I | C |
| MLflow setup | I | A/R | I | R | I |
| SeqGAN development | I | A/R | I | I | C |
| Attention visualisation | I | A/R | I | I | C |
| FastAPI development | I | C | I | A/R | I |
| Docker / DevOps | I | I | I | A/R | I |
| Streamlit UI | I | C | I | C | A/R |
| Model evaluation | C | A/R | I | I | R |
| Human evaluation | I | C | I | I | A/R |
| Documentation (all) | A/R | C | C | C | R |
| Final presentation | A | R | R | R | R |
| GitHub repository maintenance | C | R | R | A/R | C |

---

## 4. Collaboration Tools

| Tool | Purpose |
|------|---------|
| GitHub | Version control, issue tracking, pull requests |
| GitHub Projects | Kanban board, sprint planning |
| Slack / Discord | Team communication (async) |
| Google Colab / Kaggle | Shared model training notebooks |
| MLflow | Shared experiment tracking |
| Notion / Google Docs | Collaborative document drafting |
| Zoom / Google Meet | Weekly stand-ups and meetings |

---

## 5. Code Contribution Guidelines

1. All code must be committed to feature branches (`feature/task-name`) and merged via Pull Request.
2. Each Pull Request must be reviewed by at least one other team member before merge.
3. Commit messages must be descriptive: `feat: add GPT-2 fine-tuning script with MLflow logging`.
4. No direct commits to the `main` branch.
5. All Python files must follow PEP 8 style guide and include docstrings.
6. All notebooks must be cleared of cell outputs before committing (except final evaluation notebooks).

---

## Notes for Customisation

- Replace `*(Insert Name)*` with each team member's actual full name.
- If the team has fewer than 5 members, redistribute tasks from the table above — Document the redistribution explicitly.
- If roles overlap (e.g., one person handles both ML and data), note this in Section 1 and adjust the RACI accordingly.
- Add student IDs, email addresses, or contact information as required by the institution.
