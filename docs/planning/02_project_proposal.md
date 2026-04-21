# 02 — Project Proposal

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Project Proposal
**Version:** 1.0
**Date:** *(Insert submission date)*
**Team:** Team Alpha *(See assumptions below)*
**Supervisor:** *(Insert supervisor name)*

---

## Assumptions

> The following assumptions are made for documentation purposes and must be updated before final submission:
> - The project team consists of 5 members (see `04_task_assignment_and_roles.md`).
> - The project duration is approximately 16 weeks (one academic semester).
> - The primary computing resource is Google Colab Pro or an equivalent single-GPU environment.
> - The production domain is E-Commerce Product Description Generation.
> - The primary model is GPT-2 Medium (as justified in `01_recommended_model_selection.md`).

---

## 1. Project Overview

The **Automated Content Generation System** is an end-to-end AI pipeline designed to automatically generate high-quality, domain-specific product descriptions for e-commerce applications. The system accepts structured product inputs — such as product name, category, and key attributes — and produces fluent, commercially appropriate textual descriptions using a fine-tuned GPT-2 Medium language model.

The pipeline encompasses the complete machine learning lifecycle: data collection and preprocessing, model fine-tuning using Hugging Face Transformers and PyTorch, experiment tracking with MLflow, deployment via a FastAPI REST service, and a user-facing Streamlit web interface. An experimental GAN-based text generation component is also developed and evaluated to provide a principled academic comparison with the Transformer-based approach.

This project serves both as a practical engineering artefact and as an academic exploration of modern natural language generation (NLG) techniques.

---

## 2. Problem Statement

E-commerce businesses are required to maintain large product catalogues containing thousands of items, each of which demands a unique, accurate, and engaging written description. Manual content creation is labour-intensive, inconsistent in quality, and does not scale efficiently as product catalogues grow. Existing rule-based template systems produce repetitive, generic text that fails to engage consumers or perform well in search engine optimisation (SEO).

Recent advances in large language models (LLMs) and generative AI have demonstrated the potential for automated, high-quality text generation tailored to specific domains. However, many production-ready implementations rely on proprietary APIs (e.g., OpenAI GPT-4) that introduce cost, dependency, and data privacy concerns. There is a clear need for an **open-source, fine-tunable, and deployable** automated content generation solution that organisations can own and customise.

This project addresses the gap between research-level generative AI and practically deployable content generation systems by building a complete, reproducible, and academically rigorous pipeline.

---

## 3. Objectives

### 3.1 Primary Objectives

1. **Design and implement** an end-to-end automated text generation pipeline for e-commerce product descriptions.
2. **Fine-tune** a GPT-2 Medium language model on a domain-specific product description dataset.
3. **Integrate** advanced NLP techniques including attention mechanism analysis and prompt conditioning.
4. **Deploy** the system as a REST API (FastAPI) and interactive web application (Streamlit).
5. **Track** all experiments, model versions, and performance metrics using MLflow.
6. **Evaluate** the system quantitatively (Perplexity, BLEU score) and qualitatively (human evaluation).

### 3.2 Secondary Objectives

7. **Develop** an experimental GAN-based text generation module for academic comparison.
8. **Document** all design decisions, architecture choices, and implementation details to academic standard.
9. **Demonstrate** the feasibility of on-premise, open-source generative AI deployment for business use.

---

## 4. Scope

### 4.1 In Scope

- Data collection from publicly available e-commerce datasets (e.g., Amazon Product Data [Reference Needed], Open Products dataset).
- Text preprocessing pipeline: cleaning, tokenisation, deduplication, and formatting.
- Fine-tuning of GPT-2 Medium on product description data.
- Conditional generation using structured prompt templates.
- Attention visualisation module for NLP analysis.
- REST API with endpoints for text generation and health monitoring.
- Streamlit-based user interface for interactive content generation.
- MLflow experiment tracking and model registry.
- SeqGAN experimental module and comparative evaluation.
- Containerised deployment using Docker.
- Technical documentation, literature review, and final presentation.

### 4.2 Out of Scope

- Real-time integration with live e-commerce platforms (e.g., Shopify, WooCommerce API).
- Multi-language content generation (English only).
- Image-to-description multimodal generation.
- Training or fine-tuning models larger than GPT-2 Medium on standard student hardware (unless stretch goal is pursued).
- Production-scale cloud deployment with SLA guarantees.
- Commercial licensing or monetisation.

---

## 5. Expected Outcomes

Upon successful completion of this project, the following outcomes are expected:

| # | Outcome | Type |
|---|---------|------|
| 1 | Fine-tuned GPT-2 Medium model for product description generation | Technical Artefact |
| 2 | End-to-end data preprocessing and training pipeline | Technical Artefact |
| 3 | FastAPI REST service with documented endpoints | Technical Artefact |
| 4 | Streamlit web application for interactive generation | Technical Artefact |
| 5 | MLflow experiment tracking dashboard | Technical Artefact |
| 6 | SeqGAN experimental module with comparative evaluation | Technical Artefact |
| 7 | Evaluation report: Perplexity, BLEU, human evaluation | Academic Deliverable |
| 8 | Complete project documentation (9 documents) | Academic Deliverable |
| 9 | Final presentation and demonstration | Academic Deliverable |

---

## 6. Business and Academic Value

### 6.1 Business Value

| Stakeholder | Value Delivered |
|-------------|-----------------|
| E-commerce businesses | Automated, scalable product description generation; reduction in content creation cost |
| Content teams | AI-assisted drafting tool; accelerated content workflows |
| Small/medium enterprises | Accessible alternative to expensive proprietary LLM APIs |
| Data privacy-sensitive organisations | On-premise deployment; no data sent to external APIs |

**Estimated impact:** Industry studies suggest that manual product description writing costs between $5–$25 per item [Reference Needed]. For a catalogue of 10,000 products, full automation could represent savings of $50,000–$250,000, while also ensuring consistency in tone, length, and structure.

### 6.2 Academic Value

| Dimension | Contribution |
|-----------|-------------|
| NLP / Generative AI | Practical application of Transformer-based language models to domain-specific generation |
| MLOps | Demonstration of a complete, reproducible ML pipeline from raw data to deployed service |
| Comparative Study | Empirical comparison of Transformer-based vs GAN-based text generation |
| Attention Mechanisms | Visualisation and analysis of self-attention in GPT-2 Medium |
| Systems Engineering | Full-stack AI system design: data, model, API, UI, monitoring |

This project contributes to the growing body of applied NLP research and provides a reproducible baseline for future work on domain-specific language model fine-tuning.

---

## 7. Summary

The Automated Content Generation System represents a technically rigorous, practically deployable, and academically valuable graduation project. By fine-tuning a state-of-the-art Transformer-based language model on a targeted domain dataset and integrating it within a production-quality software pipeline, this project bridges the gap between academic NLP research and real-world AI deployment. The inclusion of an experimental GAN component and a comprehensive evaluation framework ensures the project meets the highest standards expected of a graduation-level submission.

---

## Notes for Customisation

- Replace all *(Insert...)* placeholders with actual names, dates, and institution information.
- Update the "business impact" cost figures with citations from current industry reports if available.
- If the domain changes from Product Description Generation, update Section 1, 2, 4, and 6 accordingly.
- The stretch goal (Mistral 7B / LLaMA-2) can be added as a separate objective under Section 3.2 if pursued.
