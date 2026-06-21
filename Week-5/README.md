# Week 5: Spark Assignment - Data Cleaning & Analysis

This folder contains my practical code and dataset for Week 5. The assignment covers basic data cleaning, handling nulls, column type casting, and running group aggregations using PySpark.

## Folder Structure
* **data/** - Holds the input dataset file (`Sample - Superstore.csv`).
* **notebook/** - Contains my execution code notebook (`spark_basics.ipynb`).
* **output/** - Contains the final output file saved after running the pipeline (`results_summary.csv`).

## Steps I Followed in the Notebook
1. **Spark Session Setup:** Started a local Spark instance in Colab and loaded the superstore dataset. I also disabled strict ANSI mode (`spark.sql.ansi.enabled` to `false`) so the code wouldn't crash on messy columns.
2. **Data Cleaning:** Used `dropDuplicates` on `Customer ID` and `Order Date` to remove duplicates, filtered out rows with missing IDs, and filled empty fields in the `Region` column with the string 'Unknown'.
3. **Data Type & Rename:** Casted the `Order Date` column into a proper timestamp data type and renamed the column to `event_time`.
4. **Fixing String Error:** Casted the `Sales` column to a double type so mathematical functions could run on it without throwing formatting errors.
5. **Queries & Aggregations:** * Found the average sales for the West region grouped by product Category.
   * Totaled order counts per City for cities with more than 10 orders.
   * Filtered data specifically for the Corporate segment where order quantities are 5 or higher.
   * Extracted summary statistics (min, max, and average) for the Sales column.
6. **Pipeline Export:** Created a final sequence to clear duplicates, fill missing sales rows with 0, calculate total revenue per Region, and exported it cleanly to a CSV inside the output folder.
