# 🚀 Test Automation Solution   
**Python | Playwright | Behave | Allure | Xray | Enterprise Architecture**

---

## 📌 Overview

This project is a **production-grade Test Automation Solution (TAS)** designed following:

- ISTQB CTAL-TAE (Test Automation Engineer) principles  
- Layered enterprise architecture  
- Hybrid testing strategy (UI + API)  

It demonstrates how to build a **scalable, maintainable, and observable automation framework** from scratch, evolving layer-by-layer.

> The framework supports **UI (Playwright), API (HTTP), and hybrid scenarios** using **BDD (Behave)** with strong **traceability and reporting (Allure + Xray)**.

---

## 🏗️ Architecture Overview

The solution follows a **multi-layer architecture**, separating concerns across business, technical, and infrastructure levels.

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

```text
Gherkin Scenario
   ↓
Tag Interpretation (@ui / @api / @hybrid)
   ↓
Lifecycle Manager initializes context
   ↓
Step Definitions
   ↓
Domain Flow (Business logic)
   ↓
Adapter (UI/API abstraction)
   ↓
Interaction Layer (Playwright / HTTP)
   ↓
State retrieval
   ↓
Assertions (DomainAssert)
   ↓
Artifacts + Logs
   ↓
Allure Report + Xray Upload
