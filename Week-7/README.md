# Week 7: Delta Lake Assignment - Incremental Data Processing

This folder contains my Week 7 Delta Lake assignment. The assignment focuses on performing incremental data processing using Delta Lake by loading customer data, cleaning it, applying the MERGE operation, and validating the final results using PySpark.

## Folder Structure

- **data/** - Contains the input datasets (`customer_master.csv` and `customer_incremental.csv`).
- **notebooks/** - Contains the implementation notebook (`delta_scd_assignment.ipynb`).
- **screenshots/** - Includes screenshots of each major step such as data loading, cleaning, Delta table creation, MERGE operation, validation, and final output.

## Steps I Followed in the Notebook

### Spark Session Setup
Created a Spark session in Google Colab using PySpark and Delta Lake libraries to enable Delta table operations.

### Data Loading
Loaded the `customer_master.csv` dataset into a PySpark DataFrame and verified the schema and total number of records.

### Data Cleaning
Checked the dataset for null values, removed any null records, and eliminated duplicate rows to prepare clean data for processing.

### Delta Table Creation
Stored the cleaned customer dataset as a Delta table, which serves as the base table for incremental processing.

### Incremental Data Processing
Loaded the `customer_incremental.csv` dataset containing updated and new customer records.

### MERGE Operation
Used the Delta Lake **MERGE** command to:
- Update existing customer records based on `customer_id`.
- Insert new customer records that were not present in the original dataset.

### Validation
Validated the processed data by:
- Checking the total number of records after the MERGE operation.
- Verifying that no duplicate `customer_id` values existed.
- Displaying the final updated Delta table.

## Learning Outcome

Through this assignment, I learned how to:
- Work with Delta Lake tables in PySpark.
- Perform basic data cleaning before processing.
- Handle incremental data using the MERGE operation.
- Update existing records and insert new records efficiently.
- Validate the final dataset to ensure data quality and consistency.
