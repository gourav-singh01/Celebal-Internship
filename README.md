# Celebal Excellence Internship Program (CEIP) 2026

This repository tracks my progress, code files, and assignments completed during my Data Engineering Internship at Celebal Technologies.

**Intern:** Gourav Singh  
**Domain:** Data Engineering  
**Timeline:** May 2026 – Present  
**Institution:** Poornima University

---

## 💡 About This Workspace

This repository contains all the assignments and practical work completed during my internship. Throughout these weekly tasks, I explored different areas of Data Engineering including data cleaning with Pandas, SQL database design, Azure cloud services, Apache Spark, and Delta Lake. Each week's folder includes the notebook, required datasets, outputs, screenshots (where applicable), and a README explaining the implementation.

---

## 🛠️ Technology Stack

- **Languages:** Python, SQL
- **Libraries & Frameworks:** Pandas, NumPy, Apache Spark (PySpark), Delta Lake
- **Databases:** SQLite3
- **Cloud Platform:** Microsoft Azure
- **Data Integration:** Azure Data Factory (ADF V2)
- **Development Environment:** Google Colab

---

# 📁 Repository Index

| Assignment Directory | Topic Focus | Core Tools Used | Status |
| :--- | :--- | :--- | :--- |
| 🚀 **[Week 1: Data Exploration & Cleaning](./Week-1/)** | Data profiling, null handling, and feature engineering. | Python, Pandas | ✅ Completed |
| 🗄️ **[Week 2: Sales Database Analysis](./Week-2/)** | Database schema creation, joins, and SQL queries. | SQLite, SQL | ✅ Completed |
| 📊 **[Week 3: Advanced SQL Analytics](./Week-3/)** | Window functions, CTEs, ranking, and analytical queries. | Advanced SQL | ✅ Completed |
| ☁️ **[Week 4: Azure Data Pipelines](./Week-4/)** | Azure Storage, Resource Groups, and ADF pipelines. | Azure Portal, ADF V2 | ✅ Completed |
| ⚡ **[Week 5: Apache Spark Fundamentals](./spark-assignment/)** | Data cleaning, transformations, and aggregations using Spark. | PySpark, Google Colab | ✅ Completed |
| 🔄 **[Week 6: Spark Architecture & Data Processing](./Week-6/)** | Spark DataFrames, transformations, filtering, and exporting processed data. | PySpark, Google Colab | ✅ Completed |
| 🪣 **[Week 7: Delta Lake Incremental Processing](./Week-7/)** | Delta tables, incremental processing, MERGE operation, and validation. | PySpark, Delta Lake | ✅ Completed |

---

# 🔍 Weekly Summary Breakdown

## 1. [Week 1: Data Exploration & Cleaning (Pandas)](./Week-1/)

Worked on exploring datasets using Pandas, cleaning missing values, and preparing the data for analysis.

**Key Steps**

- Cleaned invalid values from numeric columns.
- Created calculated columns for business analysis.
- Filtered records using multiple conditions.

---

## 2. [Week 2: Sales Database Analysis (SQL)](./Week-2/)

Built a relational database structure and practiced SQL queries using multiple tables.

**Key Steps**

- Created normalized database tables.
- Applied primary and foreign keys.
- Performed JOIN operations and transaction handling.

---

## 3. [Week 3: Advanced SQL Analytics](./Week-3/)

Worked with analytical SQL queries to generate insights from transactional datasets.

**Key Steps**

- Used CTEs for query organization.
- Applied window functions like RANK() and ROW_NUMBER().
- Generated customer ranking reports.

---

## 4. [Week 4: Azure Cloud Fundamentals & Data Pipelines](./Week-4/)

Explored Azure services and built a basic data movement pipeline using Azure Data Factory.

**Key Steps**

- Created Azure Resource Groups and Storage Accounts.
- Configured Blob Storage containers.
- Built and executed ADF copy pipelines.

---

## 5. [Week 5: Apache Spark Fundamentals](./spark-assignment/)

Performed basic data cleaning and analysis using Apache Spark.

**Key Steps**

- Removed duplicate records.
- Handled missing values.
- Converted data types.
- Performed group aggregations and summary analysis.

---

## 6. [Week 6: Spark Architecture & Data Processing](./Week-6/)

Built a simple end-to-end PySpark data processing pipeline using the Online Retail dataset.

**Key Steps**

- Loaded CSV data with schema inference.
- Selected required columns and renamed fields.
- Casted numeric columns and created the **TotalPrice** column.
- Removed null values and filtered records.
- Exported processed data in both CSV and Parquet formats.

---

## 7. [Week 7: Delta Lake Incremental Processing](./Week-7/)

Implemented incremental data processing using Delta Lake with customer datasets.

**Key Steps**

- Loaded customer data into a Delta table.
- Performed basic data cleaning and removed duplicate records.
- Used the **MERGE** operation to update existing customers and insert new records.
- Validated the final output by checking row count and duplicate customer IDs.

---

# 📌 How to Navigate

Each week's assignment is organized in its own folder. Use the **Repository Index** above to directly access any week's work. Every folder contains its notebook, datasets, outputs/screenshots (if required), and a README describing the implementation and learning outcomes.
