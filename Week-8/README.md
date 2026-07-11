# E-Commerce Analytics System

## Overview

This project was developed as part of the **Week 8 Assignment** during the **Celebal Technologies Data Engineering Internship Program**.

The objective of this project is to generate synthetic e-commerce data, clean the data using Pandas, load it into a SQL database, perform analytical queries, and generate reports through a Python command-line interface.

---

## Technologies Used

- Python
- Pandas
- Faker
- SQLite
- SQL
- Tabulate

---

## Project Structure

```
ecommerce-analytics-system/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── database/
│   └── ecommerce.db
│
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_database.py
│   └── report_cli.py
│
├── sql/
│   ├── schema.sql
│   ├── aggregations.sql
│   ├── window_functions.sql
│   ├── cohort_analysis.sql
│   └── segmentation.sql
│
├── output/
│   └── sample_reports/
│
├── requirements.txt
└── README.md
```

---

## Project Workflow

### Step 1 - Data Generation

Synthetic datasets were generated for:

- Customers
- Products
- Orders
- Order Items

The generated data also contains a few intentionally introduced inconsistencies such as:

- Duplicate records
- Missing values
- Invalid emails
- Incorrect order IDs
- Invalid date formats

---

### Step 2 - Data Cleaning

The generated datasets were cleaned using Pandas by:

- Removing duplicate records
- Handling missing values
- Standardizing date formats
- Removing invalid records
- Validating relationships between tables

The cleaned datasets are stored inside the **data/cleaned** folder.

---

### Step 3 - Database Creation

SQLite was used to create the database.

The cleaned CSV files were loaded into the database using Python.

Tables created:

- customers
- products
- orders
- order_items

---

### Step 4 - SQL Analytics

The following SQL analysis was performed:

- Revenue by Customer
- Revenue by Category
- Monthly Revenue
- Top Selling Products

Window Functions were also used for:

- Customer Ranking
- Running Total Calculation

---

### Step 5 - Customer Analysis

Basic customer analysis includes:

- Customer Segmentation
- Cohort Analysis
- Repeat vs One-Time Customers

---

### Step 6 - Command Line Reports

A Python CLI tool was created to generate reports directly from the SQLite database.

Available reports:

- Revenue
- Products
- Customers
- Segments

Example:

```bash
python scripts/report_cli.py --report revenue
```

---

## How to Run

Generate raw datasets

```bash
python scripts/generate_data.py
```

Clean datasets

```bash
python scripts/clean_data.py
```

Load SQLite database

```bash
python scripts/load_database.py
```

Generate reports

```bash
python scripts/report_cli.py --report revenue
```

---

## Sample Outputs

Sample report screenshots are available inside:

```
output/sample_reports/
```

