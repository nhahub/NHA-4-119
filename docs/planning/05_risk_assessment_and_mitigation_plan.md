# 05 — Risk Assessment & Mitigation Plan

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Risk Assessment & Mitigation Plan
**Version:** 1.0

---

## 1. Introduction

This document identifies potential risks to the successful completion of the Automated Content Generation System project, assesses their likelihood and impact, and defines concrete mitigation and contingency strategies for each. The risk register is reviewed at the end of each milestone and updated as new risks emerge.

**Risk Rating Scale:**

| Rating | Probability | Impact |
|--------|-------------|--------|
| 1 | Very Low (< 10%) | Negligible |
| 2 | Low (10–25%) | Minor |
| 3 | Medium (25–50%) | Moderate |
| 4 | High (50–75%) | Significant |
| 5 | Very High (> 75%) | Severe / Project-threatening |

**Risk Score = Probability × Impact**

| Score Range | Risk Level | Colour |
|-------------|------------|--------|
| 1–4 | Low | 🟢 Green |
| 5–9 | Medium | 🟡 Yellow |
| 10–16 | High | 🟠 Orange |
| 17–25 | Critical | 🔴 Red |

---

## 2. Risk Categories

### 2.1 Technical Risks

| ID | Risk Description | Probability (1–5) | Impact (1–5) | Score | Level | Mitigation Strategy | Contingency Plan |
|----|-----------------|-------------------|--------------|-------|-------|---------------------|------------------|
| T1 | Fine-tuning GPT-2 Medium exceeds available GPU memory (OOM error) | 3 | 4 | 12 | 🟠 High | Use gradient accumulation, FP16 mixed precision, and reduce batch size; use `accelerate` library | Fall back to DistilGPT-2 or use LoRA / PEFT for parameter-efficient fine-tuning |
| T2 | SeqGAN training instability (mode collapse, non-convergence) | 4 | 3 | 12 | 🟠 High | Implement gradient clipping, teacher forcing, and pre-training phase; use established SeqGAN codebase as reference | Limit GAN to a demonstrative prototype; focus evaluation on GPT-2 results; document instability in academic comparison |
| T3 | GPT-2 model generates incoherent or repetitive output after fine-tuning | 3 | 4 | 12 | 🟠 High | Experiment with generation parameters (temperature, top-p, repetition_penalty); perform early stopping to avoid overfitting | Switch to a better checkpoint from MLflow; reduce training epochs |
| T4 | Attention visualisation module produces incorrect or misleading outputs | 2 | 3 | 6 | 🟡 Medium | Validate against published attention visualisation examples; use BertViz or similar established library as reference | Simplify to basic heatmap visualisation using raw attention weights |
| T5 | FastAPI service has high latency (> 5 seconds per request) | 3 | 3 | 9 | 🟡 Medium | Load model once on startup; use asynchronous request handling; quantise model (INT8) if needed | Add response caching for repeated prompts; document latency as a known limitation |
| T6 | Dependency conflicts between PyTorch, Transformers, and MLflow versions | 3 | 2 | 6 | 🟡 Medium | Use a `requirements.txt` with pinned versions; test in Docker container from the beginning | Use conda environment with explicit dependency resolution |
| T7 | Dockerised deployment fails or behaves differently from development | 2 | 3 | 6 | 🟡 Medium | Test Docker build on at least two team members' machines early in Milestone 4 | Document known platform differences; provide both Docker and native installation instructions |

---

### 2.2 Data Risks

| ID | Risk Description | Probability (1–5) | Impact (1–5) | Score | Level | Mitigation Strategy | Contingency Plan |
|----|-----------------|-------------------|--------------|-------|-------|---------------------|------------------|
| D1 | Primary dataset source is unavailable or access is restricted | 3 | 4 | 12 | 🟠 High | Identify at least 3 dataset sources early in Milestone 1; test download links immediately | Use Hugging Face Hub datasets (e.g., `McAuley-Lab/Amazon-Reviews-2023`) or web-scraped product data |
| D2 | Dataset contains excessive noise, irrelevant entries, or non-English text | 3 | 3 | 9 | 🟡 Medium | Implement robust preprocessing with language detection (`langdetect`) and quality filters | Manually curate a smaller, higher-quality subset (~10,000 samples) |
| D3 | Insufficient training data (< 10,000 samples) for effective fine-tuning | 2 | 4 | 8 | 🟡 Medium | Combine multiple datasets; apply data augmentation (paraphrase generation) | Use a smaller model (DistilGPT-2) that fine-tunes well on smaller datasets |
| D4 | Dataset contains personally identifiable information (PII) or copyrighted content | 2 | 4 | 8 | 🟡 Medium | Use only publicly available, licence-permissive datasets; include a PII scan in preprocessing | Remove identified PII records; restrict dataset use to academic purposes only |
| D5 | Data imbalance across product categories | 3 | 2 | 6 | 🟡 Medium | Analyse category distribution in EDA; implement stratified sampling | Train on a balanced subset; note imbalance as a limitation |

---

### 2.3 Deployment Risks

| ID | Risk Description | Probability (1–5) | Impact (1–5) | Score | Level | Mitigation Strategy | Contingency Plan |
|----|-----------------|-------------------|--------------|-------|-------|---------------------|------------------|
| R1 | Model inference is too slow for real-time use in production | 3 | 3 | 9 | 🟡 Medium | Apply INT8 quantisation using `torch.quantization`; limit max token generation length | Implement async batch inference; cap max output at 200 tokens; document performance trade-offs |
| R2 | Streamlit UI crashes or becomes unresponsive under load | 2 | 3 | 6 | 🟡 Medium | Use lightweight Streamlit components; avoid storing large model state in session | Fall back to a minimal HTML form that calls the FastAPI endpoint directly |
| R3 | API endpoints are exposed without authentication in demonstration environment | 2 | 3 | 6 | 🟡 Medium | Add API key authentication header to FastAPI; document security requirements | Restrict demonstration to local network only; never expose model API publicly without auth |
| R4 | Cloud deployment costs exceed project budget (if cloud deployment is attempted) | 3 | 2 | 6 | 🟡 Medium | Use free-tier cloud resources (Render, Hugging Face Spaces, Google Cloud free tier) | Deploy exclusively on local machine or academic server for demonstration purposes |

---

### 2.4 Time and Resource Risks

| ID | Risk Description | Probability (1–5) | Impact (1–5) | Score | Level | Mitigation Strategy | Contingency Plan |
|----|-----------------|-------------------|--------------|-------|-------|---------------------|------------------|
| TR1 | Team member becomes unavailable due to illness or personal emergency | 2 | 4 | 8 | 🟡 Medium | Ensure knowledge sharing and code documentation throughout; no single point of failure | Redistribute tasks among remaining members; communicate with supervisor immediately |
| TR2 | Model fine-tuning takes significantly longer than estimated (compute bottleneck) | 3 | 4 | 12 | 🟠 High | Start training early in Milestone 3; book GPU resources in advance; track time per epoch | Reduce number of training epochs; use smaller dataset; use Hugging Face AutoTrain as fallback |
| TR3 | Scope creep — expanding features beyond original plan | 3 | 3 | 9 | 🟡 Medium | Strictly follow the scope defined in the Project Proposal; PM approves any scope changes | Defer additional features to a "Future Work" section in the final report |
| TR4 | Integration of multiple components takes longer than planned | 3 | 3 | 9 | 🟡 Medium | Begin integration testing in Week 11; assign a dedicated integration week (Week 12) | Cut optional features (Airflow, advanced UI animations) to prioritise core integration |
| TR5 | Academic submission deadline is stricter than anticipated | 2 | 5 | 10 | 🟠 High | Confirm all deadlines with supervisor in Week 1; build a 3-day buffer into the final week | Begin documentation finalisation in Week 14 regardless of implementation status |

---

## 3. Risk Matrix Overview

```
Impact
  5 |        |        |        |        | TR5    |
    |        |        |        |        |        |
  4 |        |        | TR1,D3 | T1,T3  |        |
    |        |        | D1,TR2 |        |        |
  3 |        |        | T2,T4  | T5,T6  | TR3,   |
    |        |        | D2,D5  | D4,R1  | TR4    |
    |        |        | R2,R3  |        |        |
  2 |        | T7     |        |        |        |
    |        | R4     |        |        |        |
  1 |        |        |        |        |        |
    +--------+--------+--------+--------+--------+
         1        2        3        4        5
                         Probability
```

| Zone | Risk IDs | Priority |
|------|----------|----------|
| 🔴 Critical (17–25) | — | Immediate action |
| 🟠 High (10–16) | T1, T2, T3, D1, TR2, TR5 | High priority — active monitoring |
| 🟡 Medium (5–9) | T4, T5, T6, T7, D2, D3, D4, D5, R1, R2, R3, R4, TR1, TR3, TR4 | Regular monitoring |
| 🟢 Low (1–4) | — | Monitor passively |

---

## 4. Risk Monitoring Plan

| Activity | Frequency | Responsible | Output |
|----------|-----------|------------|--------|
| Risk register review | End of each milestone | Project Manager | Updated risk register |
| GPU availability check | Weekly (during M3) | ML Engineer | Status report |
| Dataset accessibility check | Week 1 (before M2) | Data Engineer | Dataset availability confirmation |
| Integration status check | Weekly (during M4) | DevOps Engineer | Integration test results |
| Timeline deviation check | Weekly | Project Manager | Schedule update |

---

## 5. Overall Risk Summary

The project carries a manageable overall risk profile. The highest-priority risks are concentrated around **GPU compute availability** (T1, TR2), **model training quality** (T2, T3), **data availability** (D1), and **deadline management** (TR5). All of these risks have concrete mitigation strategies and viable fallback plans. No risks are currently rated as Critical (17–25). The risk landscape will be re-evaluated at the start of Milestone 3 when compute-intensive work begins.

---

## Notes for Customisation

- Add institution-specific risks (e.g., restricted internet access, VPN requirements for cloud tools).
- Adjust probability ratings based on actual team skill levels and available hardware.
- If the team has access to an academic HPC cluster, downgrade T1 and TR2 probability ratings.
- If using a proprietary dataset (e.g., internal company data), add a dedicated Data Privacy risk entry under Section 2.2.
