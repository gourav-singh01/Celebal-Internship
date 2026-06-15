# Week 1: Data Exploration & Cleaning (Pandas)

This folder contains the core assignment artifacts for Week 1 data profiling, handling missing values, and engineering baseline e-commerce metrics.

## 📁 Files in this Folder
* `assignment1.ipynb` - Documented Google Colab notebook tracking the entire exploratory analysis process.
* `Cleaned_Combined_dataset.csv` - The finalized clean output dataset after cleaning cycles.

## 📝 Detailed Tasks Completed
1. **Initial Exploration:** Loaded raw datasets to inspect structural shapes, null patterns, and implicit data type maps.
2. **Missing Value Imputation:** Fixed text-based null gaps with descriptive string markers and resolved missing numerical rows using median metrics to avoid statistical skewing.
3. **Deduplication:** Isolated and dropped duplicated record keys to preserve data rows sanity.
4. **Data Type Correction:** Transformed unstructured text price string schemas into standard floating-point metrics.
5. **Feature Engineering:** Calculated a calculated `total_amount` parameter calculated natively as ($price \times quantity$).
6. **Data Subsetting:** Applied conditional index masks to extract all top-performing inventory items retaining consumer ratings above a `4.0` threshold.
