# SauceDemo Web UI Test Automation Framework

A professional-grade web UI automation portfolio project built using **Python**, **Selenium 4**, and **Pytest**. This project implements industry-standard best practices, including the **Page Object Model (POM)** architectural pattern, clean path resolution, and isolated virtual environments.

---

## 🚀 Features & Architecture

* **Page Object Model (POM):** Decoupled test logic completely separated from UI layouts, ensuring structural locators and component interactions are encapsulated independently.
* **Data-Driven Core:** Execution parameters completely externalized into parameterized CSV matrices under `data/`, driving dynamic test inputs cleanly via Pytest parametrization hooks.
* **Adaptive UI Synchronization:** A custom explicit wait wrapper engine that eliminates execution flakiness caused by DOM mutations, network latency, and CSS transition animation states.
* **Externalized Environment Control (`config.json`):** Dynamic cross-browser control and variable timing values completely decoupled from Python code. The entire framework adapts immediately by mutating a single JSON matrix.
* **Unified Utility Injection (The Bundle Pattern):** Consolidates foundational interaction utilities (`WaitUtility`, `DropdownUtility`, `JavascriptUtility`, `WindowNavigation`) into a specialized `UtilityBundle` fixture, keeping test suites clean and minimizing fixture bloat.
* **Flexible Runtime Execution Profiles:** Built-in programmatic switches for executing across major rendering drivers (`Chrome`, `Firefox`) alongside optimized headless execution rules for memory-efficient testing.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Testing Framework:** Pytest
* **UI Automation:** Selenium WebDriver (v4.x+)
* **Environment Configuration:** JSON Configuration Engine
* **Dependency & Virtual Environment Control:** Pipenv
* **Reporting Tool:** Pytest-HTML

---

## 💻 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
   ```

2. **Install Dependencies**
    Ensure you have Pipenv installed globally (pip install pipenv), then establish the locked environment:
    ```bash
    pipenv install
    ```

--- 

## 🧪 Configuration & Execution

1. Setting Up Your Execution Parameters

    Adjust the application's global state natively inside config.json:
    ```json
    {
        "browser" : "Firefox",
        "explicit_wait" : 10
    }
    ```

    **Supported Browser Targets:** `Chrome`, `Firefox`, `Headless Chrome`

2. Launching Test Suites via CLI

    To ensure optimal workspace pathing resolution, execute all commands from the repository root directory using the module run flag (-m).

    * **Configured Pytest Markers:** `login`, `inventory`, `product_detail`, `checkout`, `cart`, `nav`

    **Run Specific Test Suites (Without HTML Report Generation):**
    ```bash
    pipenv run python3 -m pytest -m nav 
    ```

    **Run Specific Test Suites (With HTML Report Generation):**
    ```bash
    pipenv run python3 -m pytest -m nav --html=reports/test_nav_report.html
    ```

    **Run Full Test Matrix:**
    ```bash
    pipenv run python3 -m pytest -v
    ```

---

## 📊 Test Reporting

This architecture uses pytest-html to aggregate run metrics into a visual dashboard for triage.

    - Asset Localization: Standardized HTML summaries compile directly to the reports/ workspace folder.
    - Failure Triage: The report tracks passing steps and extracts standard Pytest execution stack traces directly into collapsible rows for debugging.

⚠️ Overwrites Notice: Regenerating execution summaries over the default file targets will refresh active tracking arrays with the absolute newest runtime metrics.