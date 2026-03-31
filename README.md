
```
# 🚀 Test Automation Solution (TAS)  
**Python | Playwright | Behave | Allure | Xray | Enterprise Architecture**

---

## 📌 Overview

This project is a **production-grade Test Automation Solution (TAS)** designed following:

- ISTQB CTAL-TAE (Test Automation Engineer) principles  
- Layered enterprise architecture 
- Hybrid testing strategy (UI + API)  

It demonstrates how to build a **scalable, maintainable, and observable automation framework** from scratch.

---

## 🏗️ Architecture Overview

### Layers

1. Test Design Layer – Gherkin scenarios (BDD)  
2. Test Orchestration Layer – Lifecycle & execution control  
3. Business / Domain Layer – Business flows & journeys  
4. Test Structure Layer – Pages, clients, adapters  
5. Automation Core Layer – Assertions, utils, sync  
6. Application Interaction Layer – Playwright UI + API  
7. Configuration Layer – Environment & runtime config  
8. Test Data Layer – Data-driven testing  
9. Execution Environment Layer – Local / Docker / CI  
10. CI/CD Layer – Pipeline execution  
11. Observability & Reporting Layer – Allure, logs, Xray  

---

## 🔁 Execution Flow

```

Gherkin Scenario
↓
Tag Interpretation (@ui / @api / @hybrid)
↓
Lifecycle Manager initializes context
↓
Step Definitions
↓
Domain Flow
↓
Adapter
↓
Interaction Layer (UI/API)
↓
Assertions
↓
Artifacts + Reports

````

---

# 🧭 How to Use This TAS

---

## 1️⃣ Create a Test Scenario (BDD)

Write your test in Gherkin inside the `features/` folder:

```gherkin
Feature: User Authentication

  @ui @smoke
  Scenario: Successful login
    Given the user navigates to login page
    When the user logs in with valid credentials
    Then the user should be logged in
````

---

## 2️⃣ Implement Step Definitions

Steps are implemented in:

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

## 3️⃣ Use Domain Layer (Business Logic)

Domain flows orchestrate business behavior:

```python
class AuthFlows:

    def open_login_page(self):
        self.auth_port.open_login()

    def login(self, user):
        self.auth_port.login(user)
```

---

## 4️⃣ Use Adapters (Bridge to UI/API)

Adapters connect domain → structure:

```python
class AuthUIAdapter(AuthPort):

    def open_login(self):
        self.page.open()

    def login(self, user):
        self.page.login(user.email, user.password)
```

---

## 5️⃣ Interaction Layer (UI/API)

Only this layer interacts with tools:

* UI → Playwright
* API → HTTP client

Example:

```python
self.page.locator("#input-email").fill(email)
```

---

## 6️⃣ Run Tests

### ▶️ UI Tests

```bash
behave --tags="@ui and @smoke" --no-capture \
  -D login_url="https://fahym8237.github.io/auth-app/login.html"
```

---

### ▶️ API Tests

```bash
behave --tags="@api and @smoke" --no-capture \
  -D api_base_url="https://restful-booker.herokuapp.com"
```

---

### ▶️ Hybrid Tests

```bash
behave --no-capture \
  -D login_url="..." \
  -D api_base_url="..."
```

---

## 7️⃣ Use Tags (Execution Control)

| Tag         | Purpose         |
| ----------- | --------------- |
| @ui         | UI tests        |
| @api        | API tests       |
| @hybrid     | UI + API tests  |
| @smoke      | Critical tests  |
| @regression | Full test suite |

---

## 8️⃣ Test Data Management

Place datasets in:

```
features/data/
```

Example:

```csv
email,password,expected
invalid@test.com,1234,error
```

---

## 9️⃣ Configuration

Pass runtime parameters:

```bash
-D browser=chromium
-D headless=true
-D api_base_url=...
```

Or environment variables:

```bash
export TAS_BROWSER=chromium
export TAS_HEADLESS=true
```

---

## 🔟 Reporting

### Allure Report

```bash
allure serve target/allure-results
```

---

## 1️⃣1️⃣ Xray Integration

```bash
python -m xray.upload_xray_results_multipart target/xray/cucumber.json
```

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

## ⚙️ Key Features

* Hybrid Testing (UI + API)
* Tag-driven execution
* Layered enterprise architecture
* Domain-driven design
* Allure reporting
* Xray integration
* Data-driven testing

---

## 📈 CI/CD Ready

Compatible with:

* GitHub Actions
* Jenkins
* Docker

Supports:

* Parallel execution
* Headless execution
* Remote environments

---

## 🎯 Design Principles

* Separation of Concerns
* Scalability
* Maintainability
* Observability

---

## 👨‍💻 Author

**Fahym Abdelfattah)**
Test Automation Engineer | ISTQB CTFL & CTAL-TAE

---
