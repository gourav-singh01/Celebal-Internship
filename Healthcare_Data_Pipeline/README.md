# 🏥 Healthcare Data Pipeline using Medallion Architecture

This project was developed as the **Final Project** during my **Data Engineering Internship at Celebal Technologies**.

The objective of this project is to build a simple healthcare data pipeline that processes raw patient data through the **Bronze, Silver, and Gold layers** of the Medallion Architecture. The final output provides clean and business-ready datasets that can be used for reporting and analytics.

---

## 📌 Project Objectives

- Build a Medallion Architecture based data pipeline
- Store raw healthcare records in the Bronze layer
- Clean and standardize the data in the Silver layer
- Generate business summary tables in the Gold layer
- Perform SQL analysis using PySpark
- Create simple visualizations for business insights

---

## 🏗️ Architecture

```
                Raw Healthcare Dataset
                        │
                        ▼
                Bronze Layer
            (Raw Data Storage)
                        │
                        ▼
                Silver Layer
      (Cleaning & Transformation)
                        │
                        ▼
                 Gold Layer
       (Business Ready Tables)
                        │
                        ▼
         SQL Analysis & Visualization
```

---

## 📂 Project Structure

```
Healthcare_Data_Pipeline/

│── Healthcare_Data_Pipeline.ipynb
│── patients_records.csv
│── README.md

├── bronze/
│     └── bronze_data.csv

├── silver/
│     └── silver_data.csv

├── gold/
│     ├── admission_summary.csv
│     ├── billing_summary.csv
│     ├── condition_summary.csv
│     ├── gender_summary.csv
│     └── hospital_summary.csv

└── screenshots/
```

---

# 📊 Dataset Information

The dataset contains healthcare records with patient information such as:

- Patient Name
- Age
- Gender
- Blood Group
- Medical Condition
- Admission Date
- Doctor
- Hospital
- Insurance Provider
- Billing Amount
- Room Number
- Admission Type
- Discharge Date
- Medication
- Test Results

---

# 🥉 Bronze Layer

The Bronze layer stores the raw healthcare dataset without modifying the original records.

### Tasks Performed

- Loaded raw CSV dataset
- Preserved original data
- Stored raw dataset for future reference

**Output**

```
bronze/bronze_data.csv
```

---

# 🥈 Silver Layer

The Silver layer focuses on cleaning and transforming the raw data.

### Tasks Performed

- Removed duplicate records
- Converted date columns into datetime format
- Standardized text formatting
- Renamed columns using snake_case
- Generated cleaned dataset

**Output**

```
silver/silver_data.csv
```

---

# 🥇 Gold Layer

The Gold layer contains business-ready summary tables.

Generated datasets include:

- Hospital Summary
- Billing Summary
- Medical Condition Summary
- Gender Summary
- Admission Type Summary

**Output**

```
gold/
```

---

# 📈 SQL Analysis

Spark SQL queries were used to analyze the processed healthcare data.

Example analyses include:

- Patient count by hospital
- Average billing amount by insurance provider
- Distribution of medical conditions
- Gender distribution
- Admission type analysis

---

# 📊 Visualizations

Basic charts were created in Databricks to visualize:

- Patients by Hospital
- Average Billing Amount
- Medical Condition Distribution
- Gender Distribution
- Admission Types

These visualizations help in understanding healthcare trends more effectively.

---

# 💻 Technologies Used

- Python
- PySpark
- Spark SQL
- Databricks Community Edition
- Pandas
- Google Colab
- Git & GitHub

---

# 📚 Data Engineering Concepts Covered

- ETL Process
- Medallion Architecture
- Bronze Layer
- Silver Layer
- Gold Layer
- Data Cleaning
- Data Transformation
- Spark SQL
- Business Aggregations
- Batch Processing

---

# 🚀 Future Improvements

Some concepts mentioned in the project documentation can be implemented in future versions:

- Delta Lake
- MERGE Operations
- SCD Type 2
- Delta Live Tables (DLT)
- AWS S3 / Azure Data Lake
- Kafka for Real-Time Streaming
- Power BI Dashboard
- Machine Learning Integration

---

# ▶️ How to Run

1. Clone the repository

```
git clone <repository-url>
```

2. Open the notebook

```
Healthcare_Data_Pipeline.ipynb
```

3. Install required libraries

```
pip install pandas pyspark
```

4. Run all notebook cells sequentially.

---

# 📌 Learning Outcome

Through this project, I gained practical understanding of:

- Building a layered data pipeline
- Data cleaning and preprocessing
- Business data aggregation
- SQL analysis using PySpark
- Working with Databricks notebooks
- Creating business-ready datasets using Medallion Architecture

---

## 👨‍💻 Author

**Gourav Singh**

B.Tech CSE (AI & ML)
Poornima University

Celebal Technologies – Data Engineering Internship 2026
