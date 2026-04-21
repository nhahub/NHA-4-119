# 06 — Key Performance Indicators (KPIs)

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Key Performance Indicators
**Version:** 1.0

---

## 1. Introduction

This document defines the measurable Key Performance Indicators (KPIs) used to evaluate the success of the Automated Content Generation System. KPIs are grouped into four categories: Model Quality KPIs, System Performance KPIs, Project Management KPIs, and User / Business KPIs. Each KPI includes a target value, measurement method, and measurement timing.

---

## 2. Model Quality KPIs

These KPIs measure the quality and effectiveness of the fine-tuned GPT-2 Medium model for product description generation.

| KPI ID | KPI Name | Description | Target Value | Measurement Method | Measurement Timing |
|--------|----------|-------------|-------------|-------------------|-------------------|
| MQ-01 | Perplexity (Test Set) | Measures the model's uncertainty in predicting the next token. Lower is better. | ≤ 30 (for fine-tuned GPT-2 Medium on domain data) | Compute using `transformers` library on held-out test set | End of Milestone 3 |
| MQ-02 | BLEU Score (BLEU-4) | Measures n-gram overlap between generated descriptions and reference descriptions. Scale: 0–100. | ≥ 15 (BLEU-4) | `sacrebleu` library; evaluated on 500 test samples | End of Milestone 3 |
| MQ-03 | Improvement over Baseline | Percentage improvement in Perplexity of fine-tuned GPT-2 Medium over pre-trained GPT-2 Medium (no fine-tuning) | ≥ 30% reduction in perplexity | Compare baseline vs fine-tuned model on test set | End of Milestone 3 |
| MQ-04 | Human Evaluation — Fluency | Average fluency rating by human evaluators on a 1–5 Likert scale | ≥ 3.5 / 5 | Survey with 5–10 evaluators; 50 generated samples per evaluator | End of Milestone 5 |
| MQ-05 | Human Evaluation — Relevance | Average relevance-to-prompt rating by human evaluators on a 1–5 Likert scale | ≥ 3.5 / 5 | Same survey as MQ-04 | End of Milestone 5 |
| MQ-06 | Human Evaluation — Commercial Usability | Percentage of generated descriptions rated as "usable as-is or with minor edits" by evaluators | ≥ 60% | Survey binary question per sample | End of Milestone 5 |
| MQ-07 | GPT-2 vs SeqGAN Perplexity Gap | Difference in perplexity between GPT-2 Medium (fine-tuned) and SeqGAN on the same test set | GPT-2 perplexity ≤ 50% of SeqGAN perplexity | Side-by-side evaluation | End of Milestone 3 |
| MQ-08 | GPT-2 vs SeqGAN BLEU Gap | Difference in BLEU-4 score between GPT-2 Medium (fine-tuned) and SeqGAN | GPT-2 BLEU ≥ 2× SeqGAN BLEU | Side-by-side evaluation | End of Milestone 3 |

---

## 3. System Performance KPIs

These KPIs measure the technical performance and reliability of the deployed system.

| KPI ID | KPI Name | Description | Target Value | Measurement Method | Measurement Timing |
|--------|----------|-------------|-------------|-------------------|-------------------|
| SP-01 | API Response Latency (P50) | Median time from API request to first response token (or full response) | ≤ 3 seconds | `pytest` + `httpx` load testing; median over 100 requests | End of Milestone 4 |
| SP-02 | API Response Latency (P95) | 95th percentile API latency | ≤ 8 seconds | Same as SP-01 | End of Milestone 4 |
| SP-03 | API Throughput | Number of generation requests the API can handle per minute | ≥ 5 requests/minute (single-GPU inference) | Load testing with `locust` or `httpx` | End of Milestone 4 |
| SP-04 | System Uptime (Demo Session) | Percentage uptime of the FastAPI service during the demonstration | 100% (during demo period) | Manual observation + health endpoint polling | Milestone 5 presentation |
| SP-05 | `/health` Endpoint Response Time | Time for the health check endpoint to respond | ≤ 100 ms | Automated test | End of Milestone 4 |
| SP-06 | Model Load Time on Startup | Time from application start to model-ready state | ≤ 30 seconds | Timed startup measurement | End of Milestone 4 |
| SP-07 | Docker Build Success Rate | Percentage of Docker builds that succeed without manual intervention | 100% on documented target OS (Ubuntu 22.04 / macOS) | CI build test | End of Milestone 4 |
| SP-08 | Unit Test Coverage | Percentage of API and inference code covered by unit tests | ≥ 80% | `pytest-cov` | End of Milestone 4 |
| SP-09 | API Error Rate | Percentage of API requests that return 5xx errors under normal usage | ≤ 1% | API logging during testing | End of Milestone 4 |
| SP-10 | Generated Output Length | Average token count per generated product description | 80–200 tokens (commercially appropriate length) | Compute over 100 test generations | End of Milestone 3 |

---

## 4. MLOps KPIs

These KPIs measure the quality and completeness of the MLOps implementation.

| KPI ID | KPI Name | Description | Target Value | Measurement Method | Measurement Timing |
|--------|----------|-------------|-------------|-------------------|-------------------|
| ML-01 | Number of Tracked Experiments | Total number of distinct training runs logged in MLflow | ≥ 10 runs (baseline + hyperparameter variants) | MLflow UI experiment count | End of Milestone 3 |
| ML-02 | Model Registry Completeness | All production and experimental model versions registered in MLflow Model Registry | 100% of trained models registered | MLflow Model Registry inspection | End of Milestone 3 |
| ML-03 | Reproducibility | Ability to reproduce a training run to within ±5% perplexity by replaying logged MLflow parameters | Reproducible within ±5% | Manual reproduction test | End of Milestone 3 |
| ML-04 | Experiment Log Completeness | Percentage of hyperparameters, metrics, and artefacts logged per MLflow run | 100% (per defined logging schema) | Checklist-based review of MLflow runs | End of Milestone 3 |
| ML-05 | Pipeline Execution Time | End-to-end time to run the full preprocessing + training + evaluation pipeline | ≤ 12 hours (on target GPU) | Timed pipeline run | End of Milestone 3 |

---

## 5. Project Management KPIs

These KPIs measure the quality of project execution against the project plan.

| KPI ID | KPI Name | Description | Target Value | Measurement Method | Measurement Timing |
|--------|----------|-------------|-------------|-------------------|-------------------|
| PM-01 | Milestone On-Time Delivery Rate | Percentage of milestones delivered by their target week | ≥ 80% (4 of 5 milestones on time) | Project Manager review against plan | End of each milestone |
| PM-02 | Documentation Completeness | All 9 documentation files completed and reviewed | 9 of 9 documents complete | Documentation review checklist | End of Milestone 5 |
| PM-03 | GitHub Commit Frequency | Average number of meaningful commits per week per team member | ≥ 3 commits/member/week during active development (Weeks 4–13) | GitHub repository statistics | Weekly |
| PM-04 | Code Review Coverage | Percentage of merged pull requests that received at least one peer review | 100% | GitHub PR review history | End of Milestone 4 |
| PM-05 | Issue Resolution Rate | Percentage of GitHub issues closed within the same sprint they were opened | ≥ 70% | GitHub issue tracker | Weekly |

---

## 6. User Experience KPIs

These KPIs measure the usability and accessibility of the Streamlit user interface.

| KPI ID | KPI Name | Description | Target Value | Measurement Method | Measurement Timing |
|--------|----------|-------------|-------------|-------------------|-------------------|
| UX-01 | UI Task Completion Rate | Percentage of new users who can successfully generate a product description within 2 minutes without instructions | ≥ 80% | Usability test with 5 evaluators | End of Milestone 4 |
| UX-02 | UI Error / Crash Rate | Number of UI errors or crashes observed during 30 minutes of continuous use | 0 crashes | Manual UI stress test | End of Milestone 4 |
| UX-03 | UI Load Time | Time from URL open to fully interactive Streamlit interface | ≤ 5 seconds | Browser developer tools | End of Milestone 4 |
| UX-04 | User Satisfaction Score | Average rating given by evaluators for overall UI satisfaction (1–5 scale) | ≥ 3.5 / 5 | Post-task survey | End of Milestone 5 |

---

## 7. KPI Summary Dashboard

| Category | KPI Count | Critical KPIs | Target Achievement |
|----------|-----------|--------------|-------------------|
| Model Quality | 8 | MQ-01, MQ-02, MQ-04 | All targets to be met by Week 15 |
| System Performance | 10 | SP-01, SP-04, SP-08 | All targets to be met by Week 13 |
| MLOps | 5 | ML-01, ML-03 | All targets to be met by Week 10 |
| Project Management | 5 | PM-01, PM-02 | Monitored continuously |
| User Experience | 4 | UX-01, UX-04 | All targets to be met by Week 15 |
| **Total** | **32** | **9 Critical** | |

---

## 8. KPI Reporting

At the end of each milestone, the Project Manager will compile a KPI status report comparing current measured values against targets. The report will flag any KPI where the target is at risk and propose a mitigation action in alignment with the Risk Assessment document (`05_risk_assessment_and_mitigation_plan.md`).

---

## Notes for Customisation

- Adjust Perplexity target (MQ-01) based on the complexity of the chosen domain dataset and the number of training epochs completed.
- Adjust BLEU target (MQ-02) if using a dataset where reference descriptions are very diverse (BLEU naturally decreases with high reference diversity).
- Add business-specific KPIs (e.g., SEO score, readability index) if deploying for a real e-commerce partner.
- If the project includes a live deployment, add availability SLA KPIs (e.g., 99.5% uptime over 30 days).
