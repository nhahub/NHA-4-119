## Automated Content Generation System


---

## Project Description

This repository contains the complete planning, research, requirements, and design documentation for the **Automated Content Generation System** — an end-to-end AI-powered pipeline that automatically generates domain-specific product descriptions using state-of-the-art generative language models.

The system leverages a fine-tuned **GPT-2 Medium** (or optionally **DistilGPT-2** for resource-constrained environments) Transformer-based model as its core production engine, complemented by an experimental GAN-based text generation component for comparative academic analysis. The project covers the full ML lifecycle: data collection and preprocessing, model fine-tuning, pipeline integration, MLOps instrumentation, REST API deployment, and a user-facing Streamlit interface.

---

## Documentation Files

| # | File | Location | Description |
|---|------|----------|-------------|
| 1 | `01_recommended_model_selection.md` | `/docs/research/` | Model selection rationale and comparison |
| 2 | `02_project_proposal.md` | `/docs/planning/` | Project overview, problem statement, objectives, scope |
| 3 | `03_project_plan.md` | `/docs/planning/` | Timeline, milestones, Gantt-style schedule |
| 4 | `04_task_assignment_and_roles.md` | `/docs/planning/` | Team roles and responsibility matrix |
| 5 | `05_risk_assessment_and_mitigation_plan.md` | `/docs/planning/` | Risk register, risk matrix, mitigation strategies |
| 6 | `06_kpis.md` | `/docs/planning/` | Key Performance Indicators |
| 7 | `07_literature_review.md` | `/docs/research/` | Academic literature review |
| 8 | `08_requirements_gathering.md` | `/docs/requirements/` | Stakeholder analysis, user stories, functional/non-functional requirements |
| 9 | `09_system_analysis_and_design.md` | `/docs/design/` | Architecture, diagrams, database design, UI/UX, deployment |

---

## Suggested Repository Folder Structure

```
automated-content-generation/
│
├── README.md
│
├── docs/
│   ├── planning/
│   │   ├── 02_project_proposal.md
│   │   ├── 03_project_plan.md
│   │   ├── 04_task_assignment_and_roles.md
│   │   ├── 05_risk_assessment_and_mitigation_plan.md
│   │   └── 06_kpis.md
│   │
│   ├── research/
│   │   ├── 01_recommended_model_selection.md
│   │   └── 07_literature_review.md
│   │
│   ├── requirements/
│   │   └── 08_requirements_gathering.md
│   │
│   └── design/
│       └── 09_system_analysis_and_design.md
│
├── src/
│   ├── data/
│   ├── model/
│   ├── api/
│   └── ui/
│
├── notebooks/
│
├── mlflow/
│
└── tests/
```

---

## Technology Stack (Summary)

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| Data Processing | Pandas, NLTK, spaCy |
| Modelling | PyTorch, Hugging Face Transformers |
| Experiment Tracking | MLflow |
| API Layer | FastAPI |
| UI | Streamlit |
| Orchestration (optional) | Apache Airflow |
| Containerisation | Docker |
| Version Control | Git / GitHub |

---

## Repository Notes

> This repository contains **project planning, research, requirements, analysis, and design documentation** for the Automated Content Generation System. All source code, notebooks, and model artefacts are intended to reside in the `/src` and `/notebooks` directories upon implementation.


