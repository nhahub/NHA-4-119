# 08 — Requirements Gathering

**Project Title:** Automated Content Generation System for E-Commerce Product Descriptions
**Document Type:** Requirements Gathering
**Version:** 1.0

---

## 1. Stakeholder Analysis

### 1.1 Stakeholder Identification

| Stakeholder ID | Stakeholder | Type | Role in Project |
|---------------|-------------|------|-----------------|
| STK-01 | E-Commerce Business Owner / Product Manager | External / Primary | End-user and primary beneficiary; defines content quality requirements |
| STK-02 | Content Writer / Marketing Team | External / Primary | Direct users of the generation interface; responsible for reviewing and publishing content |
| STK-03 | Software Developer / Integrator | External / Secondary | Consumes the REST API to integrate the system into e-commerce platforms |
| STK-04 | Data Scientist / ML Engineer (internal team) | Internal | Develops, trains, and maintains the AI models and pipeline |
| STK-05 | Project Supervisor / Academic Evaluator | Internal / Academic | Assesses project quality, academic rigour, and alignment with learning objectives |
| STK-06 | System Administrator / DevOps Engineer (internal team) | Internal | Deploys and maintains the system infrastructure |
| STK-07 | End Consumer (website shopper) | Indirect | Ultimate beneficiary of improved product descriptions; not a direct system user |

### 1.2 Stakeholder Goals, Concerns, and Benefits

**STK-01 — E-Commerce Business Owner:**

| Dimension | Detail |
|-----------|--------|
| Goals | Reduce content creation cost; increase content volume and consistency; improve SEO performance |
| Concerns | Output quality may not meet brand standards; risk of factually incorrect descriptions |
| Expected Benefits | 70–90% reduction in time spent on product description authoring; cost savings; faster time-to-market for new products |

**STK-02 — Content Writer / Marketing Team:**

| Dimension | Detail |
|-----------|--------|
| Goals | Receive high-quality drafts that require minimal editing; easy-to-use interface |
| Concerns | AI output may lack brand voice; may feel job security threatened |
| Expected Benefits | Focus creative effort on editing and brand alignment rather than first-draft generation; higher throughput |

**STK-03 — Software Developer / Integrator:**

| Dimension | Detail |
|-----------|--------|
| Goals | Clean, documented API with predictable request/response schema |
| Concerns | API downtime; changes to endpoints; lack of error documentation |
| Expected Benefits | Seamless integration into existing e-commerce backend systems |

**STK-04 — ML Engineer (Internal):**

| Dimension | Detail |
|-----------|--------|
| Goals | Reproducible experiments; clean model registry; easy model swap/upgrade |
| Concerns | Training instability; insufficient data; compute resource constraints |
| Expected Benefits | MLflow-tracked experiments; modular codebase; documented pipeline |

**STK-05 — Academic Supervisor:**

| Dimension | Detail |
|-----------|--------|
| Goals | Technically rigorous implementation; academic documentation; comparative evaluation |
| Concerns | Lack of originality; inadequate literature review; missing evaluation |
| Expected Benefits | Well-documented project demonstrating end-to-end ML system engineering competency |

---

## 2. User Stories & Use Cases

### 2.1 User Stories

**Content Writer (Primary User):**

- As a content writer, I want to enter a product name and key attributes into a web form, so that I receive a generated product description without needing to write it from scratch.
- As a content writer, I want to regenerate a description with different parameters, so that I can choose the most suitable output for my needs.
- As a content writer, I want to copy the generated description to my clipboard with one click, so that I can paste it into our content management system quickly.
- As a content writer, I want to see multiple description variants for the same product, so that I can select or combine the best elements.

**E-Commerce Developer (API User):**

- As a developer, I want to call a REST API endpoint with a product title and category, so that my platform can automatically populate product description fields at scale.
- As a developer, I want the API to return a structured JSON response with the generated text and metadata, so that I can parse and store results programmatically.
- As a developer, I want the API to include a health check endpoint, so that I can monitor system availability in my deployment pipeline.
- As a developer, I want the API to validate and reject malformed requests with informative error messages, so that I can diagnose integration issues quickly.

**ML Engineer (Internal User):**

- As an ML engineer, I want to log all training hyperparameters and metrics to MLflow automatically, so that I can compare experiments and identify the best model configuration.
- As an ML engineer, I want to register the best model in the MLflow Model Registry, so that the API can load it without hardcoded file paths.
- As an ML engineer, I want to re-run the full training pipeline with a single command, so that I can retrain on new data or updated hyperparameters efficiently.

**System Administrator:**

- As a system administrator, I want to deploy the entire system using Docker Compose with a single command, so that I can set up the system on any compatible machine without manual configuration.
- As a system administrator, I want the API to expose health and status endpoints, so that I can integrate system monitoring into existing observability tooling.

---

### 2.2 Use Case List

| UC ID | Use Case Name | Actor | Priority |
|-------|--------------|-------|---------|
| UC-01 | Generate Product Description via UI | Content Writer | Must Have |
| UC-02 | Generate Product Description via API | Developer | Must Have |
| UC-03 | Regenerate / Retry Description | Content Writer | Should Have |
| UC-04 | Adjust Generation Parameters | Content Writer / Developer | Should Have |
| UC-05 | View Model Experiment Logs | ML Engineer | Must Have |
| UC-06 | Register and Promote Model Version | ML Engineer | Must Have |
| UC-07 | Monitor System Health | System Admin / Developer | Must Have |
| UC-08 | Run Full Training Pipeline | ML Engineer | Must Have |
| UC-09 | View Attention Visualisation | ML Engineer / Academic | Should Have |
| UC-10 | Compare GPT-2 vs SeqGAN Outputs | ML Engineer / Academic | Should Have |
| UC-11 | Download Generated Descriptions (batch) | Content Writer | Could Have |
| UC-12 | Authenticate API Requests | Developer / Admin | Should Have |

---

### 2.3 Detailed Use Case Descriptions

**UC-01: Generate Product Description via UI**

| Field | Detail |
|-------|--------|
| Use Case ID | UC-01 |
| Name | Generate Product Description via UI |
| Actor | Content Writer |
| Precondition | Streamlit UI is running; FastAPI backend is reachable; model is loaded |
| Main Flow | 1. User opens Streamlit web application. 2. User enters product name (required), category (required), and key attributes (optional). 3. User clicks "Generate Description." 4. UI sends request to FastAPI `/generate` endpoint. 5. FastAPI loads model, runs inference, returns generated text. 6. UI displays generated description in a text box. 7. User reads description and optionally clicks "Copy." |
| Alternative Flow | If the backend is unavailable, display an error message: "Service unavailable. Please try again." |
| Postcondition | A product description is displayed in the UI. |
| Business Rule | Generated description must be between 50 and 300 words. |

**UC-02: Generate Product Description via API**

| Field | Detail |
|-------|--------|
| Use Case ID | UC-02 |
| Name | Generate Product Description via API |
| Actor | Developer (external system) |
| Precondition | FastAPI service is running; model is loaded at startup |
| Main Flow | 1. Developer sends HTTP POST to `/api/v1/generate` with JSON body containing `product_name`, `category`, and optional `attributes` and `max_tokens`. 2. FastAPI validates the request using Pydantic. 3. Inference engine tokenises the prompt and runs GPT-2 Medium generation. 4. FastAPI returns JSON response with `description`, `model_version`, and `generation_time_ms`. |
| Alternative Flow | If required fields are missing, return HTTP 422 with validation error details. If model is loading, return HTTP 503. |
| Postcondition | Developer receives a JSON response containing the generated description. |

**UC-07: Monitor System Health**

| Field | Detail |
|-------|--------|
| Use Case ID | UC-07 |
| Name | Monitor System Health |
| Actor | System Administrator |
| Precondition | FastAPI service is deployed |
| Main Flow | 1. Admin or monitoring tool sends HTTP GET to `/health`. 2. FastAPI returns `{"status": "ok", "model_loaded": true, "uptime_seconds": 3600}`. |
| Alternative Flow | If model is not yet loaded, return `{"status": "starting", "model_loaded": false}` with HTTP 503. |

---

## 3. Functional Requirements

### 3.1 Data Pipeline Requirements

| ID | Requirement | Priority |
|----|-------------|---------|
| FR-01 | The system shall download and store raw product description data from at least one publicly available dataset source. | Must Have |
| FR-02 | The system shall apply text cleaning operations: HTML tag removal, special character normalisation, duplicate removal, and minimum length filtering. | Must Have |
| FR-03 | The system shall tokenise text data using the GPT-2 tokeniser (`GPT2Tokenizer`) and produce input IDs and attention masks. | Must Have |
| FR-04 | The system shall split the processed dataset into training (80%), validation (10%), and test (10%) sets using stratified sampling by product category. | Must Have |
| FR-05 | The system shall construct structured prompt strings for conditional generation in the format: `"Product: {name} | Category: {category} | Description:"`. | Must Have |

### 3.2 Model Training Requirements

| ID | Requirement | Priority |
|----|-------------|---------|
| FR-06 | The system shall fine-tune GPT-2 Medium on the product description training set using the Hugging Face `Trainer` API with Causal Language Modelling objective. | Must Have |
| FR-07 | The system shall support configurable hyperparameters: learning rate, batch size, number of epochs, warmup steps, and weight decay. | Must Have |
| FR-08 | The system shall log all training hyperparameters, training loss, validation loss, and evaluation metrics to MLflow for every training run. | Must Have |
| FR-09 | The system shall save model checkpoints at configurable intervals and upon training completion. | Must Have |
| FR-10 | The system shall register the best-performing model checkpoint in the MLflow Model Registry. | Must Have |
| FR-11 | The system shall also fine-tune a DistilGPT-2 baseline model on the same dataset for comparative evaluation. | Should Have |
| FR-12 | The system shall train a SeqGAN model on the same dataset for experimental comparison. | Should Have |

### 3.3 Evaluation Requirements

| ID | Requirement | Priority |
|----|-------------|---------|
| FR-13 | The system shall compute Perplexity on the test set for each trained model. | Must Have |
| FR-14 | The system shall compute BLEU-4 score on the test set for each trained model using `sacrebleu`. | Must Have |
| FR-15 | The system shall produce attention visualisation outputs (heatmaps) for a sample of generated descriptions. | Should Have |
| FR-16 | The system shall produce a comparative evaluation report including all models and metrics. | Must Have |

### 3.4 API Requirements

| ID | Requirement | Priority |
|----|-------------|---------|
| FR-17 | The system shall expose a REST API endpoint `POST /api/v1/generate` that accepts `product_name`, `category`, `attributes` (optional), and `max_tokens` (optional) and returns a generated product description. | Must Have |
| FR-18 | The system shall expose a `GET /health` endpoint that returns the system status and model load status. | Must Have |
| FR-19 | The system shall expose a `GET /api/v1/models` endpoint that returns available model versions from the MLflow Model Registry. | Should Have |
| FR-20 | The system shall validate all API request inputs using Pydantic models and return HTTP 422 for validation failures. | Must Have |
| FR-21 | The API shall return responses in JSON format with consistent schema. | Must Have |
| FR-22 | The API shall include API key authentication for all `/api/v1/` routes. | Should Have |
| FR-23 | The API documentation shall be auto-generated and accessible at `/docs` (Swagger UI). | Must Have |

### 3.5 User Interface Requirements

| ID | Requirement | Priority |
|----|-------------|---------|
| FR-24 | The system shall provide a Streamlit web interface with input fields for product name, category, and attributes. | Must Have |
| FR-25 | The UI shall display the generated description in a text area with a one-click copy button. | Must Have |
| FR-26 | The UI shall display generation metadata: model version and generation time. | Should Have |
| FR-27 | The UI shall allow the user to adjust generation parameters: temperature, top-p, and max token length. | Should Have |
| FR-28 | The UI shall provide a "Regenerate" button that produces a new description for the same input. | Should Have |
| FR-29 | The UI shall display a loading indicator while generation is in progress. | Must Have |

### 3.6 MLOps Requirements

| ID | Requirement | Priority |
|----|-------------|---------|
| FR-30 | The system shall be fully containerised using Docker and deployable with `docker-compose up`. | Must Have |
| FR-31 | The system shall include a `requirements.txt` with pinned dependency versions. | Must Have |
| FR-32 | The MLflow tracking server shall be accessible via a local web dashboard at `http://localhost:5000`. | Must Have |
| FR-33 | The system shall support retraining the model by re-running `train.py` with updated configuration. | Should Have |

---

## 4. Non-Functional Requirements

### 4.1 Performance

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-P01 | API response latency for a standard generation request (150 tokens) shall not exceed 5 seconds at P95 under single-user load. | ≤ 5 seconds (P95) |
| NFR-P02 | The Streamlit UI shall load and become interactive within 5 seconds on a standard broadband connection. | ≤ 5 seconds |
| NFR-P03 | The system shall support at least 5 concurrent API requests without degradation in quality. | ≥ 5 concurrent requests |
| NFR-P04 | Model startup time (loading weights from disk) shall not exceed 30 seconds. | ≤ 30 seconds |

### 4.2 Scalability

| ID | Requirement |
|----|-------------|
| NFR-S01 | The API service shall be stateless, enabling horizontal scaling by running multiple container instances behind a load balancer. |
| NFR-S02 | The data preprocessing pipeline shall be capable of handling datasets up to 500,000 records without requiring code changes. |
| NFR-S03 | The system architecture shall permit model swap (e.g., replacing GPT-2 Medium with a future larger model) by changing only the model identifier in the configuration file. |

### 4.3 Reliability

| ID | Requirement |
|----|-------------|
| NFR-R01 | The system shall handle invalid inputs gracefully and return informative error messages rather than crashing. |
| NFR-R02 | The system shall not produce empty or null responses under normal operating conditions. |
| NFR-R03 | The system shall log all errors to a structured log file for post-incident analysis. |
| NFR-R04 | Unit test coverage for API and inference modules shall be ≥ 80%. |

### 4.4 Security

| ID | Requirement |
|----|-------------|
| NFR-SEC01 | API endpoints shall require authentication via a bearer token (API key) in production deployment. |
| NFR-SEC02 | The system shall not log or store user-submitted product data beyond the immediate request lifecycle unless explicitly designed to do so. |
| NFR-SEC03 | All secrets (API keys, credentials) shall be managed via environment variables or a secrets manager, not hardcoded in source code. |
| NFR-SEC04 | The Docker image shall not run as root. |

### 4.5 Maintainability

| ID | Requirement |
|----|-------------|
| NFR-M01 | All Python modules shall include docstrings and follow PEP 8 style conventions. |
| NFR-M02 | All configuration values (model name, max tokens, learning rate, etc.) shall be externalised to a YAML or `.env` configuration file. |
| NFR-M03 | The codebase shall be organised into clearly labelled modules: `data/`, `model/`, `api/`, `ui/`. |
| NFR-M04 | A `CONTRIBUTING.md` file shall document coding standards and the pull request process. |

### 4.6 Usability

| ID | Requirement |
|----|-------------|
| NFR-U01 | A new user with no prior knowledge of AI shall be able to generate a product description within 2 minutes of opening the UI, without any instructions. |
| NFR-U02 | All form fields shall include placeholder text and tooltips explaining expected inputs. |
| NFR-U03 | The UI shall display clear error messages when the backend is unavailable. |
| NFR-U04 | The generated text shall be displayed in a readable font at a minimum size of 14px. |

### 4.7 Availability

| ID | Requirement |
|----|-------------|
| NFR-AV01 | The system shall be available 100% of the time during the scheduled demonstration period (Milestone 5). |
| NFR-AV02 | The `GET /health` endpoint shall respond within 100 ms to enable automated health monitoring. |

### 4.8 Portability

| ID | Requirement |
|----|-------------|
| NFR-PO01 | The system shall run on any host operating system that supports Docker (Linux, macOS, Windows with WSL2). |
| NFR-PO02 | The system shall function without a GPU (CPU-only inference), with a documented performance trade-off. |
| NFR-PO03 | The training pipeline shall be runnable in Google Colab Pro without code modifications by changing only the data path variable. |

---

## Notes for Customisation

- Adjust priority labels (Must Have / Should Have / Could Have) based on supervisor feedback or project constraints.
- Add institution-specific non-functional requirements (e.g., GDPR compliance, university IT security policy).
- If the domain changes from product descriptions, update FR-05 (prompt template) and FR-01 (data source) accordingly.
- Add requirement IDs for any new requirements to maintain traceability to design and test artefacts.
