# 07 — Literature Review

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Literature Review
**Version:** 1.0

---

## Abstract

This literature review surveys the theoretical foundations and recent advances in automated text generation, with particular focus on neural language models, Transformer architectures, attention mechanisms, and Generative Adversarial Networks (GANs) applied to natural language generation (NLG). The review situates the Automated Content Generation System within the broader context of NLP research, justifies the selection of GPT-2 Medium as the primary model, and identifies a research gap that the proposed project addresses. Relevant evaluation frameworks, including Perplexity and BLEU, are also examined. The review draws on foundational and contemporary literature in deep learning, NLP, and MLOps.

---

## 1. Introduction to Automated Content Generation

### 1.1 Background and Motivation

Automated content generation — the task of producing coherent, contextually appropriate natural language text without direct human authoring — has emerged as one of the most commercially significant applications of artificial intelligence [Reference Needed]. E-commerce, journalism, personalised marketing, and customer service are among the sectors most actively investing in NLG technologies, driven by the exponential growth of digital content demand and the constraints of manual authoring at scale (Reiter & Dale, 2000).

Early NLG systems were predominantly rule-based, employing handcrafted templates and deterministic grammar engines to produce text from structured data (Gatt & Krahmer, 2018). While such systems are interpretable and predictable, they are inherently brittle: they fail gracefully when inputs deviate from anticipated patterns and produce text that is perceived as mechanical and repetitive. The limitations of rule-based approaches motivated the development of data-driven NLG methods, which learn generation patterns directly from large corpora of human-written text.

The advent of deep learning, and in particular the Transformer architecture (Vaswani et al., 2017), has catalysed a paradigm shift in NLG capabilities. Pre-trained large language models (LLMs) such as GPT-2 (Radford et al., 2019), GPT-3 (Brown et al., 2020), and the subsequent generation of open-source models (e.g., LLaMA, Mistral) now demonstrate generation quality that is frequently indistinguishable from human-authored text across a range of domains [Reference Needed].

### 1.2 Scope of This Review

This review covers the following areas relevant to the proposed project:

1. Foundations of Natural Language Processing (NLP) and language modelling.
2. Neural language models: from RNNs to Transformers.
3. The Transformer architecture and self-attention mechanism.
4. Autoregressive language models for open-ended generation.
5. Encoder-decoder vs decoder-only architectures.
6. Generative Adversarial Networks (GANs) for text generation.
7. Domain-specific fine-tuning of pre-trained language models.
8. MLOps frameworks for ML system deployment.
9. Evaluation metrics for NLG.
10. Research gap and justification for the proposed project.

---

## 2. Foundations of Natural Language Processing

### 2.1 Classical NLP Approaches

Natural Language Processing has historically been approached through two broad paradigms: symbolic/rule-based methods and statistical methods (Jurafsky & Martin, 2023). Rule-based systems, including finite-state automata, context-free grammars, and hand-written lexicons, dominated NLP research from the 1950s through the early 1990s. These methods were characterised by high precision in narrow domains but poor generalisation to unseen linguistic phenomena.

The statistical NLP revolution, beginning in earnest with IBM's language models for machine translation (Brown et al., 1993), shifted the focus to learning probabilistic models from large text corpora. N-gram language models became the dominant paradigm: a trigram model, for example, estimates the probability of a word given the two preceding words. Despite their simplicity and efficiency, n-gram models suffer from severe data sparsity at higher n values and cannot capture long-range dependencies within sentences [Reference Needed].

Feature-engineered machine learning models — including Naive Bayes classifiers, Support Vector Machines (SVMs), and Maximum Entropy models — were applied successfully to tasks such as text classification, named entity recognition, and sentiment analysis. However, these methods require substantial feature engineering effort and fail to leverage the full distributional semantics of language.

### 2.2 Distributed Word Representations

A pivotal contribution to modern NLP was the development of dense, distributed word representations (embeddings). Mikolov et al. (2013) introduced the Word2Vec framework, demonstrating that neural network-derived word vectors encode semantic and syntactic relationships in their geometric structure (e.g., "king" − "man" + "woman" ≈ "queen"). Subsequent work by Pennington et al. (2014) proposed GloVe, a global co-occurrence-based alternative that achieved competitive performance on word similarity benchmarks.

These fixed embedding methods, however, produced context-independent representations: the word "bank" receives the same vector regardless of whether it refers to a financial institution or a riverbank. This limitation was overcome by contextual embedding models, most notably ELMo (Peters et al., 2018), which generates representations conditioned on the full input sequence using bidirectional LSTMs.

---

## 3. Neural Language Models: From RNNs to Transformers

### 3.1 Recurrent Neural Networks and Their Limitations

Recurrent Neural Networks (RNNs) (Elman, 1990) extended feedforward neural networks to sequential data by introducing recurrent connections, allowing hidden states to carry information across time steps. Applied to language modelling, an RNN estimates the probability of the next word conditioned on all previous words, making it theoretically better suited to long-range dependencies than n-gram models.

Long Short-Term Memory (LSTM) networks (Hochreiter & Schmidhuber, 1997) addressed the vanishing gradient problem that plagued vanilla RNNs by introducing gated memory cells. LSTMs became the dominant architecture for sequence-to-sequence (seq2seq) tasks such as machine translation (Sutskever et al., 2014) and text summarisation. Gated Recurrent Units (GRUs) (Cho et al., 2014) offered a simplified alternative with comparable performance.

Despite these advances, RNN-based language models face fundamental limitations that restrict their scalability for text generation:

- **Sequential computation:** RNNs process tokens one by one, preventing parallelisation during training and creating a severe computational bottleneck for long sequences.
- **Long-range dependency degradation:** Even LSTMs struggle to propagate information across very long sequences (> 200 tokens), as information in early time steps can be diluted by many gating operations.
- **Fixed-length context bottleneck:** In encoder-decoder architectures, the entire input is compressed into a fixed-size context vector, limiting the information available to the decoder (Bahdanau et al., 2015).

### 3.2 The Attention Mechanism

The attention mechanism, introduced by Bahdanau et al. (2015) in the context of neural machine translation, addresses the context bottleneck by allowing the decoder to selectively attend to different parts of the encoder's hidden state sequence at each decoding step. Rather than compressing the encoder output into a single vector, an attention-weighted sum of encoder states is computed dynamically for each output token. This mechanism dramatically improved translation quality and inspired a generalisation to the self-attention mechanism central to Transformer models.

Luong et al. (2015) proposed simplified "global" and "local" attention variants that reduced the computational complexity of the original attention mechanism and became widely adopted in seq2seq systems. The broader impact of attention on NLP cannot be overstated: it enabled models to capture non-local syntactic and semantic relationships, and it laid the theoretical foundation for the Transformer.

---

## 4. The Transformer Architecture

### 4.1 Attention Is All You Need

Vaswani et al. (2017) proposed the Transformer architecture in the landmark paper "Attention Is All You Need," replacing recurrence entirely with multi-head self-attention. The key innovations of the Transformer include:

- **Multi-Head Self-Attention (MHSA):** Multiple attention heads allow the model to attend to different positions in the sequence simultaneously, capturing diverse syntactic and semantic relationships. Each head operates in a lower-dimensional subspace, and the outputs are concatenated and projected.
- **Positional Encoding:** Since the Transformer is permutation-invariant, sinusoidal or learned positional encodings are added to token embeddings to inject sequential information.
- **Feed-Forward Sub-Layers:** Position-wise fully connected layers are applied after each attention layer, introducing non-linearity.
- **Residual Connections and Layer Normalisation:** These stabilise training and enable very deep architectures.
- **Parallelisable Computation:** Unlike RNNs, all positions in a sequence are processed simultaneously, dramatically accelerating training on modern GPU hardware.

The original Transformer adopted an encoder-decoder architecture, with the encoder producing contextualised representations of the input sequence and the decoder generating the output sequence autoregressively, cross-attending to encoder representations at each step. This architecture proved highly effective for translation and related conditional generation tasks.

### 4.2 The Encoder-Only Paradigm: BERT

Devlin et al. (2019) introduced BERT (Bidirectional Encoder Representations from Transformers), which pre-trains a deep Transformer encoder using Masked Language Modelling (MLM) and Next Sentence Prediction (NSP) objectives. By training on masked tokens, BERT learns deeply bidirectional contextual representations: the representation of each token is conditioned on the full left and right context simultaneously.

BERT achieved state-of-the-art performance across a wide range of NLU benchmarks (GLUE, SQuAD) and became the dominant pre-training paradigm for classification, question answering, and named entity recognition tasks. However, **BERT is not suited for open-ended text generation** for the following reasons:

- BERT's encoder-only architecture is designed for understanding (discriminative) tasks, not generation (generative) tasks.
- Masked Language Modelling trains the model to fill in randomly masked positions, not to generate coherent sequences from left to right.
- Autoregressive decoding (generating one token at a time conditioned on prior tokens) is incompatible with BERT's bidirectional context.

For this reason, while BERT is an invaluable tool for NLU tasks, it is not considered for the product description generation task in this project. The appropriate paradigm for this project is the **autoregressive decoder-only architecture** exemplified by the GPT model family.

### 4.3 The Decoder-Only Paradigm: GPT Family

Radford et al. (2018) introduced GPT (Generative Pre-trained Transformer), a decoder-only Transformer pre-trained with a Causal Language Modelling (CLM) objective: predict the next token given all preceding tokens. This autoregressive objective is directly aligned with the text generation task. GPT demonstrated that large-scale pre-training followed by task-specific fine-tuning (pre-train/fine-tune paradigm) yields strong performance across diverse NLU tasks.

GPT-2 (Radford et al., 2019) scaled this approach significantly, training on 40 GB of web text (WebText corpus) at 117 M, 345 M, 762 M, and 1.5 B parameter scales. GPT-2 demonstrated remarkable zero-shot and few-shot text generation capabilities, generating coherent paragraphs on diverse topics with minimal or no task-specific supervision. Its decoder-only architecture and autoregressive generation mechanism make it the natural choice for domain-specific fine-tuning for product description generation.

GPT-3 (Brown et al., 2020) further demonstrated that scaling model size yields significant improvements in few-shot in-context learning, largely eliminating the need for fine-tuning. However, GPT-3 (175 B parameters) and its successors are not publicly available for fine-tuning, making GPT-2 the more appropriate choice for this academic project.

---

## 5. Domain-Specific Fine-Tuning of Pre-Trained Language Models

### 5.1 Transfer Learning in NLP

The pre-train/fine-tune paradigm, now standard in modern NLP, allows a model pre-trained on a large general-purpose corpus to be adapted to a specific downstream task with relatively small amounts of task-specific data (Howard & Ruder, 2018). This approach significantly reduces the data and compute requirements for domain-specific applications.

For text generation, fine-tuning a decoder-only model such as GPT-2 on domain data involves continuing the CLM pre-training objective on the target dataset. The model learns to generate text in the style and content distribution of the target domain while retaining the general linguistic knowledge acquired during pre-training.

### 5.2 Fine-Tuning GPT-2 for Product Descriptions

Several studies have demonstrated the efficacy of fine-tuned GPT-2 variants for domain-specific NLG tasks. Shao et al. (2019) fine-tuned GPT-2 for story generation [Reference Needed]; Jain et al. (2020) applied GPT-2 to medical text generation [Reference Needed]; and commercial applications in e-commerce content generation have been reported by industry practitioners [Reference Needed]. Common findings include:

- Fine-tuning on as few as 10,000–50,000 samples produces noticeable domain adaptation.
- Prompt engineering — prepending structured conditioning strings before the generated text — enables controllable generation without architectural modification.
- Hyperparameters such as learning rate (2e-5 to 5e-5), number of epochs (3–10), and weight decay significantly affect generation quality.

### 5.3 Parameter-Efficient Fine-Tuning (PEFT)

For larger models, full fine-tuning of all parameters may be computationally prohibitive. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA (Low-Rank Adaptation) (Hu et al., 2022) freeze the original model weights and inject trainable low-rank matrices into the attention layers. LoRA reduces trainable parameters by 100–10,000× while achieving comparable fine-tuning performance. For the primary model (GPT-2 Medium, 345 M parameters), full fine-tuning is feasible on a single GPU; however, LoRA is noted as the recommended approach for any stretch-goal model (e.g., Mistral 7B, LLaMA-2 7B).

---

## 6. Generative Adversarial Networks for Text Generation

### 6.1 GAN Fundamentals

Generative Adversarial Networks (Goodfellow et al., 2014) consist of two neural networks trained in adversarial competition: a generator G that produces fake samples and a discriminator D that attempts to distinguish real from generated samples. The generator is trained to maximise the probability that the discriminator misclassifies its outputs, while the discriminator is trained to classify correctly. In the equilibrium state, G produces samples indistinguishable from real data.

GANs have demonstrated spectacular success in generating high-fidelity images (Karras et al., 2019), audio, and video. However, their application to discrete text generation faces fundamental challenges.

### 6.2 Challenges of GANs for Discrete Text Generation

The primary obstacle to applying GANs to text generation is the **non-differentiability of discrete token sampling**. In image generation, the generator produces continuous-valued pixel intensities, and gradients can be back-propagated through the generator from the discriminator's output. In text generation, the generator must produce discrete symbols (words or tokens) via an argmax or sampling operation, which is not differentiable. This breaks the standard GAN training gradient signal.

Several approaches have been proposed to address this limitation:

- **SeqGAN (Yu et al., 2017):** Uses reinforcement learning (Monte Carlo tree search) to estimate the reward signal for each generated token, bypassing the non-differentiability problem. SeqGAN was a landmark paper in text GAN research but is known to be highly sensitive to hyperparameters and prone to training instability.
- **MaskGAN (Fedus et al., 2018):** Uses a mask-and-fill approach to train an actor-critic GAN on text sequences.
- **RelGAN (Nie et al., 2019):** Proposes relational memory for the generator to capture longer-range dependencies.
- **TextGAN (Zhang et al., 2017):** Uses feature matching in a continuous latent space to bypass discrete sampling.

Despite these innovations, text GANs consistently exhibit **mode collapse** (generating a narrow, repetitive set of outputs), **training instability**, and **lower generation diversity and fluency** compared to likelihood-based language models of comparable scale [Reference Needed].

### 6.3 GAN vs Transformer-Based Generation: Comparative Assessment

| Criterion | SeqGAN / Text GAN | GPT-2 Medium (Fine-tuned) |
|-----------|------------------|--------------------------|
| Training stability | Poor (mode collapse, RL reward sparsity) | Stable (maximum likelihood) |
| Generation fluency | Moderate | High |
| Long-range coherence | Poor | Good |
| Domain adaptation | Difficult | Easy (fine-tuning) |
| Evaluation | Difficult (no principled perplexity) | Principled (perplexity, BLEU) |
| Academic precedent | High (research interest) | Very high (industry standard) |
| Production suitability | Low | High |

Given these considerations, GANs are included in this project as an **experimental and comparative component** rather than as the primary generation engine. Their inclusion serves the academic purpose of empirically validating the superiority of Transformer-based approaches for this task.

---

## 7. Encoder-Decoder Models for Conditional Generation

### 7.1 T5 and BART

T5 (Raffel et al., 2020) and BART (Lewis et al., 2020) are encoder-decoder Transformer models that excel at conditional text generation tasks framed as text-to-text problems (e.g., summarisation, translation, question answering). T5 unifies all NLP tasks under a text-to-text framework, converting every task into a "given this input text, generate this output text" format. BART pre-trains the full encoder-decoder using a denoising objective, demonstrating strong performance on summarisation benchmarks.

Both models are competitive alternatives for conditional product description generation. However, in this project, the conditioning signal is relatively simple (product title + category + attributes), and the output is open-ended prose rather than a strict transformation of the input. The decoder-only, causal language modelling approach of GPT-2 is better suited to this open-ended generation scenario, and its simpler architecture facilitates direct attention mechanism analysis.

### 7.2 Instruction-Tuned Models

Instruction-tuned models such as FLAN-T5 (Chung et al., 2022) and Mistral-7B-Instruct extend pre-trained models by fine-tuning on instruction-following datasets, enabling zero-shot generalisation to new tasks specified via natural language instructions. These models represent the current state of the art in conditional generation quality. However, their complexity, resource requirements, and the engineering overhead of instruction-following evaluation are not well-matched to the scope of a student graduation project.

---

## 8. MLOps in AI Systems

### 8.1 The MLOps Paradigm

MLOps (Machine Learning Operations) refers to the set of practices for deploying and maintaining machine learning systems in production reliably and efficiently, drawing from DevOps principles and adapting them to the specific challenges of ML systems (Sculley et al., 2015; Shankar et al., 2022). Key MLOps concerns include reproducibility, experiment tracking, model versioning, continuous integration/continuous deployment (CI/CD), monitoring, and data pipeline management.

Sculley et al. (2015) identified "hidden technical debt" in ML systems, arguing that the model training code represents only a small fraction of the total system complexity; the surrounding infrastructure — data pipelines, serving infrastructure, monitoring — constitutes the majority of engineering effort. This observation motivates the MLOps emphasis in this project.

### 8.2 MLflow for Experiment Tracking

MLflow (Zaharia et al., 2018) is an open-source platform for managing the ML lifecycle, encompassing experiment tracking, code packaging, model registry, and deployment. MLflow's tracking API allows practitioners to log parameters, metrics, artefacts, and model versions programmatically during training runs, enabling systematic comparison of experiments. The MLflow Model Registry provides versioning and lifecycle management (staging, production, archived) for registered models.

In this project, all training runs are logged to MLflow, enabling:

- Reproducibility of any training configuration.
- Visual comparison of hyperparameter effects on Perplexity and BLEU.
- Promotion of the best-performing model checkpoint to "Production" status.

### 8.3 Containerisation and Deployment

Docker has become the standard mechanism for packaging ML services, ensuring that the runtime environment (Python version, library versions, OS dependencies) is consistent across development, testing, and production environments. FastAPI, a modern asynchronous Python web framework, is widely adopted for serving ML models due to its automatic OpenAPI documentation generation, type-safety via Pydantic, and high throughput via Starlette/Uvicorn (Ramírez, 2018) [Reference Needed].

---

## 9. Evaluation Metrics for Natural Language Generation

### 9.1 Perplexity

Perplexity (PPL) is an intrinsic evaluation metric derived directly from the language model's probability distribution over the test corpus. Formally, perplexity is the exponentiated average negative log-likelihood per token:

```
PPL = exp( -1/N * Σ log P(token_i | context_i) )
```

Lower perplexity indicates that the model assigns higher probability to the test data, signifying better fluency and domain fit. Perplexity is widely used as a proxy for generation quality in language modelling research. A pre-trained GPT-2 model evaluated on a specific domain dataset typically has high perplexity; after fine-tuning, perplexity drops significantly, reflecting domain adaptation. Perplexity does not, however, measure relevance to the conditioning prompt or factual accuracy.

### 9.2 BLEU Score

BLEU (Bilingual Evaluation Understudy) (Papineni et al., 2002) measures the degree of n-gram overlap between generated text and one or more reference texts. BLEU-4 considers up to 4-gram overlaps and applies a brevity penalty to discourage short outputs. Originally developed for machine translation evaluation, BLEU has been widely adapted for NLG evaluation, including text generation.

BLEU scores for open-ended text generation tasks tend to be lower than those for translation (where a closer reference match is expected), and their interpretation must account for the diversity of valid product descriptions for a given product. A BLEU-4 score of 15–25 is generally considered acceptable for open-ended domain generation tasks [Reference Needed].

**Limitations of BLEU:** BLEU is a recall-biased surface-form metric that does not capture semantic similarity, fluency, or factual correctness. It is sensitive to tokenisation and reference diversity. Newer semantic metrics such as BERTScore (Zhang et al., 2020) address some of these limitations but require additional computation.

### 9.3 Human Evaluation

Human evaluation remains the gold standard for NLG quality assessment. For this project, human evaluation is conducted along three dimensions:

- **Fluency:** Does the generated text read as natural, grammatical English?
- **Relevance:** Is the generated description relevant to the input product attributes?
- **Commercial Usability:** Could this description be used on an e-commerce platform with minimal editing?

Evaluators rate a randomly sampled set of generated descriptions on Likert scales. Inter-annotator agreement is measured using Krippendorff's alpha or Cohen's kappa to assess the reliability of the evaluation [Reference Needed].

### 9.4 BERTScore (Optional)

BERTScore (Zhang et al., 2020) computes token-level semantic similarity between generated and reference texts using contextual embeddings from a pre-trained BERT model. It correlates better with human judgements than BLEU on several NLG benchmarks and is recommended as an optional supplementary metric in this project.

---

## 10. Research Gap and Justification for the Proposed Project

The foregoing review identifies several observations that collectively justify the Automated Content Generation System as a valuable research and engineering contribution:

1. **Practical deployment gap:** The majority of academic NLG literature focuses on model performance metrics and training methods, with limited attention to the engineering of production-ready, deployable systems including APIs, containerisation, and operational monitoring. This project addresses this gap by implementing a complete MLOps pipeline.

2. **Domain-specific fine-tuning:** While GPT-2 fine-tuning has been studied in several domains, its application to e-commerce product description generation with systematic hyperparameter analysis, attention mechanism visualisation, and rigorous quantitative evaluation represents a novel contribution at the student research level.

3. **Comparative GAN study:** The co-development of a SeqGAN experimental component within the same dataset and evaluation framework provides a principled empirical comparison that is rarely conducted in applied NLG projects, adding academic rigour.

4. **Reproducibility:** The integration of MLflow experiment tracking addresses a known reproducibility crisis in ML research (Gundersen & Kjensmo, 2018), ensuring that all experimental findings are fully reproducible.

5. **Accessibility:** By using open-source models, publicly available datasets, and free-tier compute resources, this project demonstrates an accessible pathway to AI-powered content generation that does not depend on proprietary APIs, contributing to the democratisation of NLG technology for small and medium enterprises.

---

## 11. Conclusion

This review has established the theoretical and empirical foundations for the Automated Content Generation System. The evolution from rule-based NLP to statistical methods to Transformer-based language models represents a clear trajectory of increasing capability and generality. GPT-2 Medium, as a decoder-only autoregressive Transformer with strong pre-training, a well-developed fine-tuning ecosystem, and proven domain adaptation capability, is the most suitable model for this project. The limitations of GAN-based text generation — training instability, mode collapse, and poor long-range coherence — support its role as an experimental comparison rather than a production alternative. The project's MLOps emphasis, systematic evaluation framework, and practical deployment architecture address genuine gaps in the existing literature and align with current industry best practices.

---

## References

> **Note:** The following citations are representative. Full bibliographic details should be verified and completed before academic submission. Entries marked [Reference Needed] require author identification.

- Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. *ICLR 2015.*
- Brown, T. B., et al. (2020). Language models are few-shot learners. *NeurIPS 2020.*
- Cho, K., et al. (2014). Learning phrase representations using RNN encoder-decoder for statistical machine translation. *EMNLP 2014.*
- Chung, H. W., et al. (2022). Scaling instruction-finetuned language models. *arXiv:2210.11416.*
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional Transformers for language understanding. *NAACL 2019.*
- Fedus, W., Goodfellow, I., & Dai, A. M. (2018). MaskGAN: Better text generation via filling in the ______. *ICLR 2018.*
- Gatt, A., & Krahmer, E. (2018). Survey of the state of the art in natural language generation. *Journal of Artificial Intelligence Research, 61,* 65–170.
- Goodfellow, I., et al. (2014). Generative adversarial nets. *NeurIPS 2014.*
- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation, 9*(8), 1735–1780.
- Howard, J., & Ruder, S. (2018). Universal language model fine-tuning for text classification. *ACL 2018.*
- Hu, E. J., et al. (2022). LoRA: Low-rank adaptation of large language models. *ICLR 2022.*
- Jurafsky, D., & Martin, J. H. (2023). *Speech and Language Processing* (3rd ed. draft). Stanford University.
- Karras, T., Laine, S., & Aila, T. (2019). A style-based generator architecture for generative adversarial networks. *CVPR 2019.*
- Lewis, M., et al. (2020). BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. *ACL 2020.*
- Luong, M.-T., Pham, H., & Manning, C. D. (2015). Effective approaches to attention-based neural machine translation. *EMNLP 2015.*
- Mikolov, T., et al. (2013). Distributed representations of words and phrases and their compositionality. *NeurIPS 2013.*
- Nie, W., et al. (2019). RelGAN: Relational generative adversarial networks for text generation. *ICLR 2019.*
- Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). BLEU: A method for automatic evaluation of machine translation. *ACL 2002.*
- Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. *EMNLP 2014.*
- Peters, M. E., et al. (2018). Deep contextualised word representations. *NAACL 2018.*
- Radford, A., et al. (2018). Improving language understanding by generative pre-training. *OpenAI Blog.*
- Radford, A., et al. (2019). Language models are unsupervised multitask learners. *OpenAI Blog.*
- Raffel, C., et al. (2020). Exploring the limits of transfer learning with a unified text-to-text Transformer. *JMLR, 21*(140).
- Reiter, E., & Dale, R. (2000). *Building Natural Language Generation Systems.* Cambridge University Press.
- Sculley, D., et al. (2015). Hidden technical debt in machine learning systems. *NeurIPS 2015.*
- Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to sequence learning with neural networks. *NeurIPS 2014.*
- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS 2017.*
- Yu, L., et al. (2017). SeqGAN: Sequence generative adversarial nets with policy gradient. *AAAI 2017.*
- Zaharia, M., et al. (2018). MLflow: A platform for the machine learning lifecycle. *NeurIPS Systems for ML Workshop.*
- Zhang, T., et al. (2017). Adversarial feature matching for text generation. *ICML 2017.*
- Zhang, T., et al. (2020). BERTScore: Evaluating text generation with BERT. *ICLR 2020.*

---

## Notes for Customisation

- Replace all `[Reference Needed]` citations with actual paper references found via Google Scholar, Semantic Scholar, or arXiv.
- Expand Section 5.2 with specific empirical results from published papers on GPT-2 fine-tuning for NLG tasks if available.
- Add a section on ethics and bias in language models (Bender et al., 2021 — "Stochastic Parrots") if required by the supervisor.
- For a full academic submission, use BibTeX or a citation manager and adhere to the institution's preferred citation style (APA, IEEE, etc.).
