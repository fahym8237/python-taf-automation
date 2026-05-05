# 🚀 TAS (Test Automation Solution) – UI & API Automation Framework

A modern, enterprise-grade **Test Automation Solution (TAS)** designed following **ISTQB CTAL-TAE principles**, supporting both **UI and API testing**, with full integration into:

* ✅ **Playwright (UI + API)**
* ✅ **Behave (BDD)**
* ✅ **Allure Reporting**
* ✅ **Xray Test Management (Jira)**
* ✅ **GitHub Actions CI/CD**
* ✅ **Traceability & Observability**

---

# 📌 Overview

This TAS provides a **layered architecture** to ensure:

* Maintainability
* Scalability
* Reusability
* Full traceability from requirements → execution → reporting

It supports:

* 🔹 UI Testing (Playwright)
* 🔹 API Testing (Playwright API)
* 🔹 BDD Scenarios (Behave)
* 🔹 Parallel-ready execution
* 🔹 CI/CD integration
* 🔹 Enterprise reporting (Allure + Xray)

---

# 🧱 Architecture

The framework follows a **multi-layer TAS design** check the development repo < https://github.com/fahym8237/python-taf-automation >:

```
Test Design Layer (BDD - Gherkin)
        ↓
Test Orchestration Layer (Behave + Lifecycle)
        ↓
Domain Layer (Business flows)
        ↓
Test Structure Layer (Adapters)
        ↓
Automation Core Layer (Assertions, utilities)
        ↓
Application Interaction Layer
    - UI (Playwright)
    - API (Playwright APIRequestContext)
        ↓
Configuration Layer
        ↓
Test Data Management Layer
        ↓
Execution Environment Layer
        ↓
CI/CD Layer (GitHub Actions)
        ↓
Observability & Reporting Layer
        ↓
Governance Layer
```

---

# 🧪 Supported Testing Types

## ✅ UI Testing

* Playwright browser automation
* Page Object + Adapter pattern
* Trace & screenshot capture on failure

## ✅ API Testing

* REST API testing (CRUD operations)
* Request/response capture
* Validation via Domain Assertions

---

# 🧾 Reporting

## 🔹 Allure Report

* Step-level visibility
* Attachments (screenshots, traces, API logs)
* Environment metadata

## 🔹 Xray (Jira Integration)

* Automatic Test Execution creation
* Scenario → Test mapping
* Execution results upload
* Requirement traceability via tags:

```gherkin
@PYT-1
@trace=REQ-BOOKING-CRUD-001
```

---

# 🔁 CI/CD Integration

## GitHub Actions Workflows

### ✔ API Pipeline

```
.github/workflows/api-smoke.yml
```

### ✔ UI Pipeline

```
.github/workflows/ui-smoke.yml
```

### ✔ Allure Report Publishing

```
.github/workflows/allure-pages.yml
```

---

# 🌐 Live Allure Report

After CI execution, reports are published automatically:

```
https://<username>.github.io/<repo-name>/
```

Includes:

* API report
* UI report

---

# ⚙️ Setup

## 1. Clone repository

```bash
git clone <repo-url>
cd <repo>
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
python -m playwright install
```

---

# ▶️ Run Tests Locally

## API Tests

```bash
behave --tags="@api and @smoke" --no-capture \
  -D api_base_url="https://restful-booker.herokuapp.com" \
  -D api_ignore_https_errors=true \
  -f allure_behave.formatter:AllureFormatter \
  -o target/allure-results
```

## UI Tests

```bash
behave --tags="@ui and @smoke" --no-capture \
  -D login_url="https://fahym8237.github.io/auth-app/login.html" \
  -D forgot_url="https://fahym8237.github.io/auth-app/forgot-password.html" \
  -D register_url="https://fahym8237.github.io/auth-app/register.html" \
  -D browser="chromium" \
  -D headless=false \
  -f allure_behave.formatter:AllureFormatter \
  -o target/allure-results
```

---

# 📊 Generate Allure Report (Local)

```bash
allure generate target/allure-results --clean -o target/allure-report
allure open target/allure-report
```

---

# 🧩 Xray Integration

## Required Environment Variables

Set in CI or locally:

```bash
XRAY_CLIENT_ID=
XRAY_CLIENT_SECRET=
XRAY_PROJECT_KEY=PYT
XRAY_EXECUTION_ISSUE_TYPE="Test Execution"
XRAY_ENVIRONMENT=QA
```

---

## Upload Execution Results

```bash
python scripts/filter_xray_cucumber_results.py \
  target/xray/cucumber.json \
  target/xray/cucumber.executed.json

python -m scripts.upload_xray_results_multipart \
  target/xray/cucumber.executed.json
```

---

# 📁 Project Structure

```
tas/
  core/
  domain/
  structure/
  interaction/
  orchestration/
  config/
  observability/

features/
  ui/
  api/

scripts/
  upload_xray_results_multipart.py
  filter_xray_cucumber_results.py

target/
  artifacts/
  xray/
  allure-results/
  allure-report/
```

---

# 🧠 Key Features

* ✔ Layered TAS architecture (ISTQB aligned)
* ✔ UI + API unified framework
* ✔ Domain-driven design
* ✔ Custom assertion DSL
* ✔ Tag-based execution (@ui, @api, @smoke, @regression)
* ✔ Traceability to requirements
* ✔ CI/CD ready
* ✔ Observability (logs, artifacts, traces)

---

# 🚀 Roadmap

* [ ] Parallel execution
* [ ] Test data service (externalized)
* [ ] Test Plan integration (Xray)
* [ ] Flaky test detection
* [ ] Performance testing extension

---

# 👤 Author

**Fahym Abdelfattah**
Test Automation Engineer
ISTQB CTFL & CTAL-TAE Certified

---

# 📜 License

This project is for educational and professional demonstration purposes.
