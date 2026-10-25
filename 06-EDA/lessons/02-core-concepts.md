# Exploratory Data Analysis (EDA)

EDA is a documented investigation of data quality, distributions, relationships, and possible modelling risks before drawing conclusions.

## Workflow
1. Define the question and unit of analysis.
2. Load data and preserve a raw copy.
3. Inspect dimensions, column names, types, and sample rows.
4. Check missingness, duplicates, invalid values, and inconsistent categories.
5. Summarize distributions and outliers.
6. Compare relevant groups and examine relationships.
7. Check leakage, sampling bias, and time-related issues.
8. Record findings, limitations, and next steps.

## Missing values and outliers
Missingness can be random or systematically related to a variable. Do not automatically drop every row. Investigate why values are missing and compare strategies. Outliers may be errors or valid rare events; verify before removing them.

## Leakage and split strategy
Data leakage occurs when information unavailable at prediction time influences training. Split before fitting transformations. For time series, use chronological splits rather than random shuffling when future observations must be predicted.

## Deliverable
A useful EDA report includes the question, data dictionary, quality checks, charts, key findings, limitations, and reproducible code.
