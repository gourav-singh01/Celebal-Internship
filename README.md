# Celebal Excellence Internship Program (CEIP) 2026

This repository tracks my progress, code files, and assignments completed during my Data Engineering Internship at Celebal Technologies.

**Intern:** Gourav Singh  
**Domain:** Data Engineering  
**Timeline:** May 2026 – Present  
**Institution:** Poornima University  

---

## 💡 About This Workspace
This repository acts as my complete project portfolio for the internship tasks. It includes everything I have worked on, from basic data cleaning with Pandas and building database structures in SQL, to cloud data movement using Azure and distributed cluster handling with PySpark.

---

## 🛠️ Technology Stack
* **Languages:** Python, SQL
* **Libraries & Engines:** Pandas, NumPy, Apache Spark (PySpark), Google Colab
* **Databases:** SQLite3 (Schema Design, Joins, Transactions)
* **Cloud Platform:** Microsoft Azure (Storage Accounts, Resource Groups, IAM)
* **Data Integration:** Azure Data Factory (ADF V2 - Pipelines, Activities, Datasets)

---

## 📁 Repository Index

| Assignment Directory | Topic Focus | Core Tools Used | Status |
| :--- | :--- | :--- | :--- |
| 🚀 **[Week 1: Data Exploration & Cleaning](./Week-1/)** | Data profiling, fixing null values, and making basic features. | Python, Pandas, Google Colab | Completed |
| 🗄️ **[Week 2: Sales Database Analysis](./Week-2/)** | Database tables setup, primary/foreign keys, and joins. | SQLite, Relational SQL | Completed |
| 📊 **[Week 3: Advanced SQL Analytics](./Week-3/)** | Window functions, CTE loops, and ranking data. | Advanced SQL | Completed |
| ☁️ **[Week 4: Serverless Data Pipelines](./Week-4/)** | Setting up cloud storage and building ADF pipelines. | Azure Portal, ADF V2 | Completed |
| ⚡ **[Week 5: Apache Spark Fundamentals](./spark-assignment/)** | Cleaning messy data files and running group aggregations. | PySpark, Google Colab | Completed |

---

## 🔍 Weekly Summary Breakdown

### 1. [Week 1: Data Exploration \& Cleaning (Pandas)](./Week-1/)
Worked on exploring data tables using Pandas, filling missing blank values, and cleaning columns for basic e-commerce records.
* **Key Steps:**
  * Cleaned garbage text characters out of the price column and converted it to float numbers.
  * Created a new calculated column for `total_amount` by multiplying price and quantity.
  * Filtered data to find top rows where the product rating was higher than 4.0.

### 2. [Week 2: E-Commerce Sales Database Analysis (SQL)](./Week-2/)
Worked on creating a database structure, linking tables together securely, and practicing safe transaction management.
* **Key Steps:**
  * Made four separate tables (`customers`, `products`, `orders`, `order_items`) linked together with primary and foreign keys.
  * Wrote queries using `INNER JOIN` and `LEFT JOIN` to combine data across tables.
  * Practiced safe data queries using `BEGIN TRANSACTION`, `COMMIT`, and `ROLLBACK` blocks to prevent data mistakes.

### 3. [Week 3: Advanced SQL Analytics \& Insights](./Week-3/)
Focused on breaking down transactional data into cleaner logic blocks using window functions and subqueries.
* **Key Steps:**
  * Used `SELECT DISTINCT` to extract unique tracking segments from a flat file.
  * Applied window functions like `RANK()` and `ROW_NUMBER()` to analyze customer purchase order timelines.
  * Built a top-10 customer leaderboard using a single clean CTE block.

### 4. [Week 4: Azure Cloud Fundamentals \& Data Pipelines](./Week-4/)
Worked on setting up storage layers in the cloud and making copy pipelines inside Azure Data Factory.
* **Key Steps:**
  * Created an Azure Resource Group named `rg-celebal-week4` in the East US region.
  * Set up a storage account (`stcelebalweek4`) and added a container to store raw input files.
  * Built an ADF data pipeline (`pl_process_superstore`) that uses a Get Metadata check before triggering a data copy task.
  * Managed access permissions using basic Access Control (IAM) settings.

### 5. [Week 5: Apache Spark Fundamentals](./spark-assignment/)
Worked on loading messy data files into Spark, fixing string type issues, and running aggregation queries.
* **Key Steps:**
  * Removed duplicate data rows using combined `Customer ID` and `Order Date` columns.
  * Changed the data configurations (`spark.sql.ansi.enabled` to `false`) to smoothly handle text lines sitting inside numeric columns without crashing.
  * Converted the `Sales` column data type to double and ran group summaries to find average sales per Category and total revenue per Region.

### 6. [Week 6: Spark Architecture & Data Processing](./Week-6/)
Worked on building a complete PySpark data processing pipeline by loading retail data, applying transformations, handling missing values, and saving processed output in different file formats.

* **Key Steps:**
  * Loaded the dataset with proper schema inference, selected required columns, and renamed columns for better readability.
  * Casted numeric data types, created a new `TotalPrice` column, removed null values, and filtered records using multiple conditions.
  * Saved the processed dataset in both CSV and Parquet formats while using Spark actions like `.show()` and `.count()` for efficient execution.
---

## 📌 How to Navigate
You can click directly on any of the bold folder links in the **Repository Index** table above to jump straight to that assignment directory. Each folder has its own short README file explaining the setup and code logic!
