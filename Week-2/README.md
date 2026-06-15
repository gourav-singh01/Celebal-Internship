# Week 2: E-Commerce Sales Database Analysis (SQL)

This folder tracks relational schema architecture designs, database constraints testing, and business intelligence queries using SQLite.

## 📁 Files in this Folder
* `Assignment2.ipynb` - Notebook detailing initial database profiling, target schema declarations, and foundational aggregates.
* `SQL_Task2_Week2.ipynb` - Complete transaction script processing all 27 custom business queries requested in the evaluation criteria.
* `cleaned_superstore.csv` - The source dataset mapped directly to the database staging engine.

## 📝 Detailed Tasks Completed
1. **Relational Schema Design:** Structured standard staging operational tables (`customers`, `products`, `orders`, `order_items`).
2. **Data Integrity Gates:** Enforced foundational relational logic using explicit `PRIMARY KEY`, `FOREIGN KEY` tracking rules, and logical `CHECK` constraint boundaries.
3. **Granular Filtering:** Constructed deep analytical `WHERE` selection logic to sort items across granular categorical blocks.
4. **Group-Level Aggregates:** Gathered business metric clusters by grouping transactional attributes via `SUM`, `AVG`, `COUNT`, `MIN`, and `MAX` calls.
5. **Multi-Table Normalization:** Linked separate dimensional footprints back together using relational `INNER JOIN` and `LEFT JOIN` syntax blocks.
6. **Conditional Mapping:** Applied logical conditional logic branches using `CASE WHEN` workflows to dynamically evaluate operational records.
7. **Transactional ACID Control:** Formed explicit execution transaction scripts using safe `BEGIN TRANSACTION`, `COMMIT`, and conditional error `ROLLBACK` commands.
