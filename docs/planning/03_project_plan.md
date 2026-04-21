# 03 — Project Plan

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Project Plan
**Version:** 1.0
**Total Duration:** 16 Weeks (1 Academic Semester)
**Start Date:** *(Insert Week 1 date)*
**End Date:** *(Insert Week 16 date)*

---

## Assumptions

> - Project duration: 16 weeks.
> - Team size: 5 members.
> - Primary development environment: Google Colab Pro, local Python environment, GitHub for version control.
> - Project follows a hybrid Agile/milestone-based approach with 5 major milestones.
> - All team members contribute part-time (~15–20 hours/week average).

---

## 1. Project Overview

This plan organises the 16-week project into five sequential milestones, each with clearly defined objectives, tasks, deliverables, and expected outputs. A Gantt-style schedule table is provided at the end of this document.

---

## 2. Milestones

### Milestone 1 — Project Initiation & Research (Weeks 1–3)

**Objective:** Establish project foundations, finalise scope, complete literature review, and select the core model.

| # | Task | Responsible Role | Output |
|---|------|-----------------|--------|
| 1.1 | Define problem statement, objectives, and scope | Project Manager | Project Proposal (02_project_proposal.md) |
| 1.2 | Conduct literature review on NLP, Transformers, GANs | Research Lead | Literature Review (07_literature_review.md) |
| 1.3 | Evaluate and select production model (GPT-2 Medium) | ML Engineer | Model Selection doc (01_recommended_model_selection.md) |
| 1.4 | Set up GitHub repository and project folder structure | DevOps Engineer | GitHub repo with initial structure |
| 1.5 | Identify datasets (Amazon Product Data, Open Products) | Data Engineer | Dataset shortlist with sources |
| 1.6 | Complete requirements gathering and stakeholder analysis | Systems Analyst | Requirements doc (08_requirements_gathering.md) |
| 1.7 | Draft system analysis and design (architecture) | Systems Analyst | Initial design document |
| 1.8 | Define KPIs and risk assessment | Project Manager | KPI doc, Risk doc |

**Key Deliverables:**
- Project Proposal
- Literature Review
- Model Selection Rationale
- Initial Requirements Document
- Risk Assessment
- GitHub Repository (initialised)

---

### Milestone 2 — Data Collection & Preprocessing (Weeks 4–6)

**Objective:** Acquire, clean, and prepare the training dataset for model fine-tuning.

| # | Task | Responsible Role | Output |
|---|------|-----------------|--------|
| 2.1 | Download and explore raw e-commerce dataset | Data Engineer | Raw dataset files |
| 2.2 | Perform Exploratory Data Analysis (EDA) | Data Engineer + ML Engineer | EDA notebook |
| 2.3 | Implement text cleaning pipeline (remove HTML, special chars) | Data Engineer | `preprocess.py` script |
| 2.4 | Tokenise data using GPT-2 tokeniser (`GPT2Tokenizer`) | ML Engineer | Tokenised dataset |
| 2.5 | Split into train/validation/test sets (80/10/10) | ML Engineer | Split dataset files |
| 2.6 | Design and implement prompt template for conditioning | ML Engineer | Prompt template specification |
| 2.7 | Implement data loader using Hugging Face `datasets` library | ML Engineer | `DataLoader` module |
| 2.8 | Document data pipeline and data schema | Systems Analyst | Data documentation section |

**Key Deliverables:**
- Cleaned and tokenised dataset
- EDA notebook
- Data preprocessing pipeline (`preprocess.py`)
- Data schema documentation
- Train/validation/test splits

---

### Milestone 3 — Model Development & Training (Weeks 7–10)

**Objective:** Fine-tune GPT-2 Medium, develop the GAN experimental module, and track all experiments.

| # | Task | Responsible Role | Output |
|---|------|-----------------|--------|
| 3.1 | Set up MLflow tracking server and experiment logging | DevOps Engineer + ML Engineer | MLflow server running; experiment tracked |
| 3.2 | Implement fine-tuning script using Hugging Face `Trainer` API | ML Engineer | `train.py` |
| 3.3 | Run baseline fine-tuning (GPT-2 Medium, default hyperparameters) | ML Engineer | Baseline model checkpoint |
| 3.4 | Perform hyperparameter tuning (LR, batch size, epochs) | ML Engineer | Optimised model checkpoint |
| 3.5 | Implement attention visualisation module | ML Engineer + Research Lead | `attention_viz.py` |
| 3.6 | Implement SeqGAN experimental module | ML Engineer | `seqgan.py` (experimental) |
| 3.7 | Train SeqGAN on same dataset | ML Engineer | GAN model checkpoint |
| 3.8 | Compare GPT-2 Medium vs DistilGPT-2 baseline vs SeqGAN | Research Lead | Comparison table |
| 3.9 | Register best model in MLflow Model Registry | DevOps Engineer | Registered model artefact |

**Key Deliverables:**
- Fine-tuned GPT-2 Medium model (production)
- Fine-tuned DistilGPT-2 (baseline)
- SeqGAN experimental model
- MLflow experiment logs and runs
- Hyperparameter tuning report
- Attention visualisation outputs

---

### Milestone 4 — System Integration & Deployment (Weeks 11–13)

**Objective:** Build the REST API and UI, integrate all components, containerise, and deploy.

| # | Task | Responsible Role | Output |
|---|------|-----------------|--------|
| 4.1 | Implement FastAPI REST service (`/generate`, `/health`, `/docs`) | Backend Developer | `api/main.py` |
| 4.2 | Integrate model loading and inference within FastAPI | Backend Developer + ML Engineer | Inference module |
| 4.3 | Write unit and integration tests for API endpoints | Backend Developer | `tests/` directory |
| 4.4 | Build Streamlit web interface | Frontend/UI Developer | `ui/app.py` |
| 4.5 | Connect Streamlit UI to FastAPI backend | Frontend/UI Developer | Integrated UI–API |
| 4.6 | Write Dockerfile for API service and UI | DevOps Engineer | `Dockerfile`, `docker-compose.yml` |
| 4.7 | Configure Docker Compose for multi-service orchestration | DevOps Engineer | `docker-compose.yml` |
| 4.8 | (Optional) Set up Airflow DAG for pipeline orchestration | DevOps Engineer | `airflow/dags/pipeline_dag.py` |
| 4.9 | End-to-end integration testing | All | Integration test report |
| 4.10 | Deploy to staging environment | DevOps Engineer | Running staging deployment |

**Key Deliverables:**
- FastAPI REST service
- Streamlit web application
- Dockerised deployment stack
- API documentation (auto-generated by FastAPI)
- Integration test report
- Staging deployment (local or cloud VM)

---

### Milestone 5 — Evaluation, Documentation & Presentation (Weeks 14–16)

**Objective:** Evaluate the system, finalise all documentation, and prepare the final presentation.

| # | Task | Responsible Role | Output |
|---|------|-----------------|--------|
| 5.1 | Compute Perplexity on test set for all models | ML Engineer | Evaluation metrics table |
| 5.2 | Compute BLEU scores on held-out test samples | ML Engineer | BLEU score report |
| 5.3 | Conduct human evaluation (survey with 5–10 evaluators) | Research Lead | Human evaluation results |
| 5.4 | Compile comparative evaluation report | Research Lead + ML Engineer | Evaluation report |
| 5.5 | Finalise and review all 9 documentation files | Project Manager | Final documentation package |
| 5.6 | Prepare GitHub repository for submission | DevOps Engineer | Clean, documented GitHub repo |
| 5.7 | Prepare final presentation slides | All | Presentation deck |
| 5.8 | Conduct dry-run presentation | All | Rehearsal feedback |
| 5.9 | Final submission and presentation | All | Submitted project |

**Key Deliverables:**
- Full evaluation report (Perplexity, BLEU, human evaluation)
- Final versions of all 9 documentation files
- Clean GitHub repository
- Final presentation slides
- Submitted project package

---

## 3. Deliverables Summary

| Milestone | Deliverable | Due (Week) |
|-----------|-------------|-----------|
| M1 | Project Proposal, Literature Review, Model Selection, Requirements, Risk/KPI docs | Week 3 |
| M2 | Processed dataset, EDA notebook, preprocessing pipeline | Week 6 |
| M3 | Fine-tuned models, MLflow logs, experimental GAN, attention visualisation | Week 10 |
| M4 | FastAPI service, Streamlit UI, Docker stack, integration tests | Week 13 |
| M5 | Evaluation report, final documentation, presentation | Week 16 |

---

## 4. Resource Allocation

| Role | Assigned To | Primary Responsibilities | Tools |
|------|------------|--------------------------|-------|
| Project Manager | Member 1 | Planning, coordination, documentation oversight | GitHub Projects, Notion |
| ML Engineer | Member 2 | Model fine-tuning, training scripts, evaluation | PyTorch, Hugging Face, MLflow |
| Data Engineer | Member 3 | Data collection, preprocessing, EDA | Pandas, NLTK, spaCy |
| Backend / DevOps Engineer | Member 4 | API development, Docker, deployment | FastAPI, Docker, Airflow |
| Research Lead / UI Developer | Member 5 | Literature review, attention analysis, Streamlit UI | Streamlit, LaTeX/Markdown |

> **Note:** Team member names are not specified. Assign real names before submission.

---

## 5. Gantt-Style Schedule

| Task | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 | W13 | W14 | W15 | W16 |
|------|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|
| **M1: Initiation & Research** | | | | | | | | | | | | | | | | |
| Project Proposal | ██ | ██ | | | | | | | | | | | | | | |
| Literature Review | ██ | ██ | ██ | | | | | | | | | | | | | |
| Model Selection | | ██ | ██ | | | | | | | | | | | | | |
| Requirements & Design | | ██ | ██ | | | | | | | | | | | | | |
| Risk & KPI Docs | | | ██ | | | | | | | | | | | | | |
| **M2: Data Collection** | | | | | | | | | | | | | | | | |
| Dataset acquisition & EDA | | | | ██ | ██ | | | | | | | | | | | |
| Preprocessing pipeline | | | | ██ | ██ | ██ | | | | | | | | | | |
| Tokenisation & splits | | | | | ██ | ██ | | | | | | | | | | |
| **M3: Model Development** | | | | | | | | | | | | | | | | |
| MLflow setup | | | | | | | ██ | | | | | | | | | |
| GPT-2 Medium fine-tuning | | | | | | | ██ | ██ | ██ | | | | | | | |
| Hyperparameter tuning | | | | | | | | ██ | ██ | ██ | | | | | | |
| SeqGAN experimental | | | | | | | | ██ | ██ | ██ | | | | | | |
| Attention visualisation | | | | | | | | | ██ | ██ | | | | | | |
| **M4: Integration & Deployment** | | | | | | | | | | | | | | | | |
| FastAPI development | | | | | | | | | | | ██ | ██ | | | | |
| Streamlit UI | | | | | | | | | | | ██ | ██ | | | | |
| Docker / DevOps | | | | | | | | | | | | ██ | ██ | | | |
| Integration testing | | | | | | | | | | | | ██ | ██ | | | |
| **M5: Evaluation & Submission** | | | | | | | | | | | | | | | | |
| Evaluation (BLEU, PPL) | | | | | | | | | | | | | | ██ | ██ | |
| Final documentation | | | | | | | | | | | | | | ██ | ██ | ██ |
| Presentation prep | | | | | | | | | | | | | | | ██ | ██ |
| Final submission | | | | | | | | | | | | | | | | ██ |

> **Legend:** ██ = Active work in that week.

---

## 6. Communication Plan

| Activity | Frequency | Format | Participants |
|----------|-----------|--------|-------------|
| Team stand-up | Weekly | Video call / in-person | All team members |
| Supervisor meeting | Bi-weekly | Scheduled meeting | Team + Supervisor |
| Code review | Per milestone | GitHub Pull Request | ML Engineer + DevOps |
| Progress report | End of each milestone | Markdown update in GitHub | Project Manager |
| Final review | Week 15 | Full team session | All team members |

---

## Notes for Customisation

- Replace week numbers with actual calendar dates aligned with your academic semester.
- Update team member names in the Resource Allocation table.
- Adjust Gantt chart task durations based on actual sprint velocity after Week 4.
- Add a buffer week (e.g., Week 17) if the institution permits extended deadlines.
