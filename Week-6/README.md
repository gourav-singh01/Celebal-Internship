# Week 6 - Spark Architecture & Data Processing

**Name:** Gaurav
**Domain:** Data Engineering
**Internship:** Celebal Technologies Internship 2026

## Objective

The objective of this assignment was to understand Apache Spark and build a simple data processing pipeline using PySpark. The work includes reading data, applying transformations, filtering records, handling null values, creating new columns, and saving the processed data in different file formats.

---

## Dataset

This assignment uses the **Online Retail Dataset**.

The dataset is publicly available and can be downloaded from:

**https://archive.ics.uci.edu/ml/datasets/online+retail**

> **Note:** The original dataset has not been included in this repository because it exceeds GitHub's web upload size limit. 

---

## Tasks Performed

* Read the CSV file using PySpark
* Loaded data with `header=True` and `inferSchema=True`
* Displayed sample records and schema
* Selected only the required columns
* Renamed a column
* Casted numeric columns to appropriate data types
* Created a new calculated column (`TotalPrice`)
* Removed rows containing null values
* Filtered the dataset based on given conditions
* Saved the processed data in both **CSV** and **Parquet** formats
* Used `.show()` for previewing data instead of `.collect()`

---

## Project Structure

```text
Week6_Spark_Assignment
│
├── notebook
│   └── Week6_Spark_Assignment.ipynb
│
├── output
│   ├── csv
│   └── parquet
│
└── README.md
```

---

## Output

The processed dataset was successfully generated and saved in both CSV and Parquet formats. The notebook contains the execution results, including sample outputs and schema.

---

## Technologies Used

* Python
* Apache Spark (PySpark)
* Google Colab

---


---

## Learning Outcomes

Through this assignment, I gained practical experience with:

* Spark DataFrames
* Data transformations and actions
* Schema inference and type casting
* Handling null values
* Filtering datasets
* Writing data in CSV and Parquet formats
* Building a simple end-to-end PySpark data pipeline
