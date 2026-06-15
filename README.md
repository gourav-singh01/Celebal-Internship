# Celebal Excellence Internship Program (CEIP) 2026

Welcome to my core repository tracking my progress, data pipelines, and database architecture workflows during the 2026 Data Engineering Internship at Celebal Technologies.

**Intern:** Gourav Singh  
**Domain:** Data Engineering  
**Timeline:** May 2026 – Present  
**Institution:** Poornima University  

---

## 💡 About This Workspace
This workspace serves as a centralized, production-grade portfolio demonstrating my technical progression in processing massive datasets, constructing relational data layers, optimizing analytical queries, and orchestrating serverless data movement pipelines across the cloud. All tasks focus on transforming unstructured raw data streams into reliable, business-ready insight matrices.

---

## 🛠️ Unified Technology Stack
* **Languages & Scripting:** Python, Structured Query Language (SQL)
* **Data Processing Engines:** Pandas, NumPy, Google Colab
* **Database Infrastructures:** SQLite3, Relational Schema Normalization, ACID Transactions
* **Cloud Architecture:** Microsoft Azure Portal (Resource Groups, Storage Accounts, IAM)
* **Data Ingestion & ETL:** Azure Data Factory (ADF V2), Linked Services, Dataset Schemas, Control Flows

---

## 📁 Interactive Repository Index

| Assignment Directory | Core Focus Area | Primary Technical Tools | Status |
| :--- | :--- | :--- | :--- |
| 🚀 **[Week 1: Data Exploration & Cleaning](./Week-1/)** | Data profiling, handling missing values, and feature engineering. | Python, Pandas, Google Colab | ⁠Completed |
| 🗄️ **[Week 2: Sales Database Analysis](./Week-2/)** | Relational schema enforcement, multi-table joins, and ACID handling. | SQLite, Relational SQL | Completed |
| 📊 **[Week 3: Advanced SQL Analytics](./Week-3/)** | Analytical window functions, complex CTE loops, and client leaderboards. | Advanced SQL, Norm Engines | Completed |
| ☁️ **[Week 4: Serverless Data Pipelines](./Week-4/)** | Cloud storage setups, logical checking gates, and end-to-end ADF pipelines. | Azure Portal, ADF V2 | Completed |

---

## 🔍 Deep Dive Module Summaries

### 1. [Week 1: Data Exploration \& Cleaning (Pandas)](./Week-1/)
Focused on inspecting structural anomalies within unstructured transactional datasets, implementing data imputation strategies, and crafting core feature metrics.
* **Key Achievements:**
  * Handled string price columns, cleansing garbage symbols and casting them into standard floats.
  * Engineered an operational `total_amount` parameter calculated natively via ($price \times quantity$).
  * Extracted high-performing inventory segments using targeted logical masks (Rating > 4.0).

### 2. [Week 2: E-Commerce Sales Database Analysis (SQL)](./Week-2/)
Focused on mapping relational operational blueprints, building data integrity walls, and testing secure, fault-tolerant database modifications.
* **Key Achievements:**
  * Created normalized database systems spanning separate `customers`, `products`, `orders`, and `order_items` instances locked under strict `PRIMARY KEY` and `FOREIGN KEY` constraints.
  * Formed multi-table analytical query traces using high-performance `INNER JOIN` and `LEFT JOIN` operations.
  * Modeled a safe database state change routine by writing explicit `BEGIN TRANSACTION`, `COMMIT`, and error-catching `ROLLBACK` transaction flows.

### 3. [Week 3: Advanced SQL Analytics \& Insights](./Week-3/)
Focused on deep schema decomposition, nested execution hierarchies, isolated Common Table Expressions (CTEs), and complex partitioning metrics.
* **Key Achievements:**
  * Utilized `SELECT DISTINCT` parameters to transform flat transactional data streams into decoupled analytical dimension components.
  * Applied window functions like `RANK()` and `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date)` to compile chronological client profiles.
  * Built an absolute Top-10 customer spending leaderboard tracking complex joins and a single consolidated execution CTE.

### 4. [Week 4: Azure Cloud Fundamentals \& Serverless Data Pipelines](./Week-4/)
Focused on organizing distributed cloud instances, structuring object-based data landings, and engineering metadata validation gates using serverless orchestration engines.
* **Key Achievements:**
  * Provisioned a centralized resource perimeter group container (`rg-celebal-week4`) inside the `East US` regional cloud network plane.
  * Mounted a General-Purpose V2 storage account (`stcelebalweek4`) hosting a private `raw-data` binary container path.
  * Developed an integration data pipeline (`pl_process_superstore`) linking an automated on-success validation trigger from a `Get Metadata` block into a downstream copy task.
  * Audited group-level access matrix parameters via `Access Control (IAM)` to enforce security best practices.

---

## 📌 Navigation Guide
To check out individual execution files, source files, or specific assignments, click directly on any of the folder title links in the **Interactive Repository Index** above. Each directory is backed by its own **dedicated README.md mini-homepage** tracking its specific technical metrics, code environments, and project summaries!
