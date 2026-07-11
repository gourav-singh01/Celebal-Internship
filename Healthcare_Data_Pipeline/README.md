# Healthcare Data Pipeline using Medallion Architecture

## Project Overview

This project demonstrates the implementation of a Healthcare Data Pipeline using the Medallion Architecture (Bronze, Silver, and Gold layers). The objective is to process raw healthcare patient records, clean and transform the data, and generate business-ready insights through SQL analysis and visualizations.

The project was developed in Google Colab using Python and follows a simple ETL workflow.

---

## Project Objectives

- Store raw healthcare data without modifications.
- Clean and standardize the dataset.
- Create business summary tables for analysis.
- Perform SQL-based data analysis.
- Visualize important healthcare insights.

---

## Technology Stack

- Python
- Pandas
- DuckDB (SQL)
- Matplotlib
- Google Colab

---

## Project Workflow

```
Patients Dataset (.csv)
        │
        ▼
Bronze Layer (Raw Data)
        │
        ▼
Silver Layer (Data Cleaning & Transformation)
        │
        ▼
Gold Layer (Business Summary Tables)
        │
        ▼
SQL Analysis
        │
        ▼
Data Visualization
```

---

## Project Structure

```
Healthcare_Data_Pipeline/
│
├── Healthcare_Data_Pipeline.ipynb
├── README.md
├── patients_records.csv
│
├── bronze/
│   └── bronze_data.csv
│
├── silver/
│   └── silver_data.csv
│
└── gold/
    ├── hospital_summary.csv
    ├── billing_summary.csv
    ├── condition_summary.csv
    ├── gender_summary.csv
    └── admission_summary.csv
```

---

## Bronze Layer

- Stores the original healthcare dataset.
- No modifications are made.
- Maintains raw data for future reference.

---

## Silver Layer

- Removes duplicate records.
- Checks missing values.
- Converts date columns into datetime format.
- Standardizes text values.
- Renames column names using snake_case.

---

## Gold Layer

Business-ready summary tables were created for analysis:

- Hospital Summary
- Billing Summary
- Medical Condition Summary
- Gender Summary
- Admission Type Summary

---

## SQL Analysis

SQL queries were performed to analyze:

- Total Patients
- Average Age
- Gender Distribution
- Medical Condition Analysis
- Hospital-wise Patient Count
- Average Billing
- Admission Type Distribution
- Insurance Provider Analysis
- Test Results Distribution
- Highest Billing Patients

---

## Data Visualization

The project includes visualizations for:

- Top Hospitals by Patient Count
- Gender Distribution
- Medical Condition Distribution
- Admission Type Distribution
- Average Billing by Hospital
- Test Results Distribution

---

## Conclusion

This project demonstrates a simple healthcare data pipeline using the Medallion Architecture. The raw data was processed through Bronze, Silver, and Gold layers to generate meaningful business insights using SQL queries and data visualizations.

---

## Future Scope

- Implement the pipeline using Apache Spark and Delta Lake.
- Store data in cloud storage such as AWS S3 or Azure Data Lake.
- Create interactive dashboards using Power BI or Tableau.
- Automate the pipeline using scheduling tools.
