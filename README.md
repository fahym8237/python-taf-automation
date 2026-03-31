# 🚀 Test Automation Solution (TAS)  
**Python | Playwright | Behave | Allure | Xray | Enterprise-Grade Architecture**

---

## 📌 Overview

This repository contains a **production-ready Test Automation Solution (TAS)** designed using:

- **ISTQB CTAL-TAE best practices**
- **Layered enterprise architecture**
- **Hybrid automation strategy (UI + API)**

The objective of this project is to demonstrate how to build a **scalable, maintainable, and observable automation framework** aligned with real-world enterprise standards.

---

## 🎯 Objectives

- Build a **modular and extensible automation framework**
- Support **UI, API, and Hybrid testing**
- Enable **high observability (logs, artifacts, reports)**
- Ensure **CI/CD readiness**
- Follow **clean architecture & domain-driven design**

---

## 🏗️ Architecture Overview

This TAS is designed using a **layered architecture**, where each layer has a clear responsibility:

### 🔹 Core Layers

1. **Test Design Layer**  
   → Gherkin (BDD) scenarios defining business behavior

2. **Test Orchestration Layer**  
   → Controls lifecycle, hooks, execution flow

3. **Domain Layer (Business Logic)**  
   → Encapsulates business flows (e.g., authentication, booking)

4. **Test Structure Layer**  
   → Pages, API clients, adapters

5. **Automation Core Layer**  
   → Assertions, utilities, synchronization logic

6. **Interaction Layer**  
   → Direct interaction with:
   - Playwright (UI)
   - HTTP clients (API)

7. **Configuration Layer**  
   → Environment & runtime configuration

8. **Test Data Layer**  
   → External datasets (CSV, JSON)

9. **Execution Environment Layer**  
   → Local / Docker / CI execution

10. **CI/CD Layer**  
   → Pipeline integration (GitHub Actions, Jenkins)

11. **Observability Layer**  
   → Logging, artifacts, Allure reporting, Xray integration

---

## 🔁 Execution Flow (Critical for Understanding)

Below is the **end-to-end execution lifecycle of a test scenario**:

```
Gherkin Scenario
↓
Tag Interpretation (@ui / @api / @hybrid)
↓
Lifecycle Manager initializes execution context
↓
Step Definitions (BDD glue code)
↓
Domain Layer (business flows)
↓
Adapters (bridge domain → implementation)
↓
Interaction Layer (Playwright / API client)
↓
State retrieval (UI/API response)
↓
Assertions (validation)
↓
Artifacts & Logs generation
↓
Reporting (Allure) + Test Management (Xray)
```

### 🧠 Key Insight

> The **Domain Layer is fully decoupled** from UI/API tools — making the framework scalable and maintainable.

---

# 🧭 How to Use This TAS

---

## 1️⃣ Write a Test Scenario (BDD)

Create Gherkin scenarios inside:

```
features/
```

```gherkin
Feature: User Authentication

  @ui @smoke
  Scenario: Successful login
    Given the user navigates to login page
    When the user logs in with valid credentials
    Then the user should be logged in
```

---

## 2️⃣ Implement Step Definitions

Location:

```
features/steps/
```

Example:

```python
@given("the user navigates to login page")
def step_impl(context):
    context.auth_flow.open_login_page()
```

---

## 3️⃣ Use Domain Layer (Business Abstraction)

Encapsulate business logic:

```python
class AuthFlows:

    def open_login_page(self):
        self.auth_port.open_login()

    def login(self, user):
        self.auth_port.login(user)
```

---

## 4️⃣ Use Adapters (Domain → Implementation)

Adapters connect domain logic to UI/API:

```python
class AuthUIAdapter(AuthPort):

    def open_login(self):
        self.page.open()

    def login(self, user):
        self.page.login(user.email, user.password)
```

---

## 5️⃣ Interaction Layer (Low-Level Execution)

Only this layer interacts with tools:

- UI → Playwright
- API → HTTP Client

```python
self.page.locator("#input-email").fill(email)
```

---

## 6️⃣ Execute Tests

### ▶️ UI Tests

```bash
behave --tags="@ui and @smoke" --no-capture \
  -D login_url="https://your-app-url"
```

---

### ▶️ API Tests

```bash
behave --tags="@api and @smoke" --no-capture \
  -D api_base_url="https://restful-booker.herokuapp.com"
```

---

### ▶️ Hybrid Tests (UI + API)

```bash
behave --no-capture \
  -D login_url="..." \
  -D api_base_url="..."
```

---

## 7️⃣ Tag-Driven Execution

| Tag         | Description              |
|------------|--------------------------|
| @ui        | UI scenarios             |
| @api       | API scenarios            |
| @hybrid    | Combined UI + API        |
| @smoke     | Critical validation      |
| @regression| Full test suite          |

---

## 8️⃣ Test Data Management

Store datasets in:

```
features/data/
```

Example:

```csv
email,password,expected
invalid@test.com,1234,error
```

---

## 9️⃣ Configuration Management

### CLI Parameters

```bash
-D browser=chromium
-D headless=true
-D api_base_url=...
```

### Environment Variables

```bash
export TAS_BROWSER=chromium
export TAS_HEADLESS=true
```

---

## 🔟 Reporting & Observability

### 📊 Allure Report

```bash
allure serve target/allure-results
```

Includes:

- Steps
- Attachments
- Logs
- Screenshots

---

## 1️⃣1️⃣ Xray Integration (JIRA)

```bash
python -m xray.upload_xray_results_multipart target/xray/cucumber.json
```

Supports:

- Test execution tracking
- Traceability
- CI integration

---

## 📂 Project Structure

```
tas/
├── orchestration/
├── domain/
├── structure/
├── core/
├── interaction/
├── config/
├── data/
├── observability/

features/
├── *.feature
├── steps/
├── data/

target/
├── allure-results/
├── xray/
├── artifacts/
```

---

## ⚙️ Key Capabilities

- ✅ Hybrid Testing (UI + API)
- ✅ Layered Architecture (Enterprise-grade)
- ✅ Domain-driven design
- ✅ Tag-based execution control
- ✅ Data-driven testing
- ✅ Allure reporting
- ✅ Xray integration
- ✅ CI/CD ready

---

## 🚀 CI/CD Compatibility

Fully compatible with:

- GitHub Actions  
- Jenkins  
- Docker  

Supports:

- Parallel execution  
- Headless execution  
- Remote browser execution  

---

## 🎯 Design Principles

- **Separation of Concerns**
- **Scalability**
- **Maintainability**
- **Observability**
- **Reusability**

---

## 👨‍💻 Author

**Fahym Abdelfattah**  
Test Automation Engineer  
ISTQB CTFL | CTAL-TAE

---
