# 01 — Recommended Model Selection

**Project:** Automated Content Generation System
**Domain:** Product Description Generation
**Document Type:** Model Selection Rationale
**Version:** 1.0

---

## 1. Purpose of This Document

This document presents a technically justified recommendation for the primary generative language model to be used in the Automated Content Generation System. The selection is based on four criteria: technical suitability for the task, practical performance, feasibility within a student project context, and academic value. The chosen model will serve as the **main production model** throughout all project documentation and implementation.

---

## 2. Task Definition

The target task is **domain-specific product description generation**: given a short product title and optionally a set of key attributes (e.g., category, features), the system should produce a coherent, fluent, and commercially appropriate multi-sentence product description.

This is a **conditional, open-ended text generation** task, which places the following demands on the model:

- Strong language fluency and coherence across multiple sentences.
- Ability to be fine-tuned on domain-specific data (e-commerce product descriptions).
- Autoregressive (left-to-right) text generation capability.
- Manageable parameter count for fine-tuning on consumer-grade or free-tier GPU hardware.
- Good support within the Hugging Face `transformers` ecosystem.

---

## 3. Recommended Model: GPT-2 Medium

### 3.1 Model Overview

| Property | Value |
|----------|-------|
| Model Family | GPT-2 (OpenAI, open-sourced) |
| Variant | GPT-2 Medium |
| Parameters | ~345 million |
| Architecture | Transformer Decoder (autoregressive) |
| Pre-training Objective | Causal Language Modelling (CLM) |
| Hugging Face ID | `gpt2-medium` |
| Licence | Modified MIT |

GPT-2 Medium is a decoder-only Transformer language model pre-trained on the WebText corpus (~40 GB of filtered web text). Its autoregressive generation mechanism is inherently aligned with free-form text generation tasks. The medium-sized variant strikes the optimal balance between generation quality and fine-tuning feasibility on hardware commonly available to students (e.g., Google Colab Pro, Kaggle Kernels, or a single NVIDIA T4/V100 GPU).

### 3.2 Justification for Selection

1. **Architectural fit.** GPT-2 is a causal language model; it generates each token conditioned on all previous tokens. This is the correct inductive bias for product description generation, where the model must produce coherent, forward-flowing prose rather than fill in masked tokens.

2. **Fine-tuning tractability.** With 345 M parameters, GPT-2 Medium can be fine-tuned end-to-end on a dataset of ~50,000–100,000 product descriptions within 3–6 hours on a single A100 (or 8–12 hours on a T4), which is realistic for a semester-length project.

3. **Ecosystem maturity.** The model is natively supported by Hugging Face `transformers`, `datasets`, and `Trainer` API, which dramatically reduces boilerplate code and enables reproducible experiments.

4. **Academic precedent.** Numerous published works use GPT-2 variants for domain-specific text generation, ensuring a rich body of literature to situate the project academically.

5. **Controllability.** Conditional generation can be implemented by prepending structured prompts (e.g., `"Product: Wireless Headphones | Category: Electronics | Description:"`) before fine-tuning, giving the model a clear conditioning signal without requiring architectural modification.

6. **Interpretability add-ons.** Attention weights are accessible via the Hugging Face API, enabling the attention-mechanism analysis component required by the project specification.

---

## 4. Comparison with Alternative Models

### 4.1 Alternative 1 — DistilGPT-2

| Criterion | DistilGPT-2 | GPT-2 Medium |
|-----------|-------------|--------------|
| Parameters | ~82 M | ~345 M |
| Generation quality | Moderate | Good |
| Fine-tuning time | Very fast | Moderate |
| Academic value | Low–Moderate | Moderate–High |
| Recommended use | Prototyping / low-resource fallback | **Production model** |

**Assessment:** DistilGPT-2 is suitable for rapid prototyping or environments with no GPU. For a graduation-level project, its generation quality is insufficient for a convincing production demonstration. It is retained in this project as a **lightweight baseline** for benchmarking.

---

### 4.2 Alternative 2 — GPT-2 Large / XL

| Criterion | GPT-2 Large (774 M) | GPT-2 XL (1.5 B) | GPT-2 Medium |
|-----------|---------------------|-------------------|--------------|
| Parameters | 774 M | 1.5 B | 345 M |
| Generation quality | Very good | Excellent | Good |
| VRAM required (fine-tune) | ~24 GB | ~40 GB+ | ~10–12 GB |
| Student-feasible? | Borderline | No | **Yes** |
| Training time (T4 GPU) | 24–48 h | 80 h+ | 8–12 h |

**Assessment:** GPT-2 Large produces noticeably better text but requires hardware (A100 40 GB or multi-GPU) that is not reliably available to most student teams. GPT-2 XL is prohibitive. For a graduation project, the diminishing returns in quality do not justify the compute cost. GPT-2 Medium is the pragmatic optimum.

---

### 4.3 Alternative 3 — FLAN-T5 (Encoder-Decoder)

| Criterion | FLAN-T5-Base | FLAN-T5-Large | GPT-2 Medium |
|-----------|--------------|---------------|--------------|
| Architecture | Encoder–Decoder (seq2seq) | Encoder–Decoder | Decoder-only |
| Strengths | Instruction-following, conditional | High-quality conditional | Open-ended CLM |
| Parameters | 250 M | 780 M | 345 M |
| Task fit | Conditional generation (good) | Conditional generation (excellent) | Open-ended + conditional (good) |
| Fine-tuning complexity | Moderate | High | Low–Moderate |
| Academic alignment | Good (seq2seq) | Good | **Strong (CLM, attention)** |

**Assessment:** FLAN-T5 is a legitimate alternative, especially for strictly conditional tasks. However, the project specification explicitly requires attention mechanism analysis and positions the model within the GPT/autoregressive paradigm common in industry-level content generation systems. GPT-2 Medium's decoder-only architecture is more illustrative of the generation mechanisms typically discussed in NLP courses and literature.

---

### 4.4 Alternative 4 — LLaMA-2 / Mistral 7B (Instruction-Tuned)

| Criterion | Mistral 7B | GPT-2 Medium |
|-----------|-----------|--------------|
| Parameters | 7 B | 345 M |
| Generation quality | State-of-the-art | Good |
| Fine-tuning approach | QLoRA / LoRA | Full fine-tune or LoRA |
| VRAM required | ~16–24 GB (QLoRA) | ~10–12 GB |
| Complexity for student project | High | **Low–Moderate** |
| Licence | Restricted commercial use | Modified MIT |
| Academic value | Very high | High |

**Assessment:** Models such as Mistral 7B or LLaMA-2 7B produce outstanding results and could represent the gold standard for this domain. If the project team has access to an A100 GPU (e.g., via institutional HPC), a LoRA fine-tune of Mistral 7B would be academically impressive. However, for teams relying on Google Colab or Kaggle free tier, this approach introduces significant engineering overhead and instability. **This model is noted as an optional stretch-goal upgrade**, but GPT-2 Medium remains the primary model for reliability and reproducibility.

---

## 5. GAN Component

As specified in the project brief, a **GAN-based text generation component** will be developed as an **experimental/comparison module**, not as the core production engine. The GAN architecture (likely a SeqGAN or TextGAN variant) will be trained on the same product description dataset and evaluated using the same metrics (BLEU, Perplexity) to provide a quantitative comparison against the Transformer-based approach. The known limitations of GANs for discrete text (mode collapse, training instability, non-differentiability of token sampling) are expected to be demonstrated empirically, reinforcing the academic argument for Transformer-based approaches.

---

## 6. Final Decision

| Role | Model |
|------|-------|
| **Main Production Model** | GPT-2 Medium (`gpt2-medium`) |
| Lightweight Baseline | DistilGPT-2 (`distilgpt2`) |
| Experimental / Comparison | SeqGAN (custom PyTorch implementation) |
| Optional Stretch Goal | Mistral 7B with LoRA (if GPU resources allow) |

> **All subsequent project documentation, architecture diagrams, pipeline designs, API specifications, and evaluation plans are based on GPT-2 Medium as the primary model.**

---

## Notes for Customisation

- If the project supervisor recommends a specific model (e.g., T5, BART, or a domain-specific variant), replace `gpt2-medium` with the recommended Hugging Face model ID throughout all documents.
- If GPU resources change (e.g., access to A100 cluster), upgrade the production model to `mistralai/Mistral-7B-v0.1` with LoRA, and update the fine-tuning sections accordingly.
- The DistilGPT-2 baseline can be swapped for `gpt2` (117 M) if a slightly stronger baseline is desired.
