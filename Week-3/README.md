# Week 3: Advanced SQL Analytics & Insights

This folder focuses on optimized analytical workflows, including subqueries, recursive common table expressions, window routing functions, and a customer spending mini-project.

## 📁 Files in this Folder
* `SQL_Assignment_Week3.ipynb` - Script matrix mapping advanced join frameworks and complex nested blocks.
* `SQL_Task_Week3.ipynb` - Mini-project execution notebook resolving specific corporate buyer segment performance metrics.

## 📝 Detailed Tasks Completed
1. **Database Normalization:** Executed `SELECT DISTINCT` queries to parse raw un-normalized transactional data blocks into three decoupled clean tables (`customers`, `products`, `orders`).
2. **Deep Subquery Nesting:** Built operational evaluation subqueries to extract orders yielding revenues strictly above the enterprise-wide average transaction benchmark.
3. **Common Table Expressions (CTEs):** Formed isolated query logic architectures using `WITH` statement blocks to preprocess user spending tables.
4. **Window Analytical Functions:** 
   * Deployed `RANK() OVER (ORDER BY TotalSales DESC)` to compile a global client ledger.
   * Utilized `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date)` to rank chronologically every purchase event within a user's timeline.
5. **Leaderboard Scripting:** Integrated multi-table joins, optimized processing CTEs, and `DENSE_RANK()` logic blocks into a single query to output a top-10 customer leaderboard.
