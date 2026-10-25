# NumPy and Pandas — Core Concepts

## NumPy
NumPy provides efficient N-dimensional arrays and vectorized numerical operations. An array generally stores values of a compatible dtype and avoids Python-level loops for many operations.

```python
import numpy as np
values = np.array([10, 20, 30, 40])
print(values.mean())       # 25.0
print(values * 2)          # [20 40 60 80]
print(values[values > 20]) # [30 40]
```

## Pandas
A `Series` is a labeled one-dimensional array. A `DataFrame` is a labeled table of columns.

```python
import pandas as pd
df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Mina"],
    "age": [21, None, 24],
    "score": [88, 75, 93],
})
print(df.head())
print(df.isna().sum())
```

## Inspect before changing data
Use `df.shape`, `df.info()`, `df.describe()`, `df.dtypes`, and `df.isna().sum()` before cleaning. Never assume missing values or duplicate records should always be deleted; understand the business meaning first.

## Common cleaning workflow
1. Load data with `pd.read_csv`.
2. Inspect shape, columns, types, missing values, and duplicates.
3. Normalize column names.
4. Parse dates and convert numeric columns carefully.
5. Handle missing values with a documented rule.
6. Check duplicates and impossible values.
7. Save a clean output and retain the raw source.

## Grouping and joining
```python
summary = df.groupby("city", dropna=False)["sales"].agg(["count", "mean", "sum"])
merged = customers.merge(orders, on="customer_id", how="left", validate="one_to_many")
```
Use `validate` when possible to detect unexpected join cardinality.

## Practice
- Create a DataFrame with missing values.
- Calculate grouped averages.
- Merge customer and order tables.
- Explain why the raw dataset should be preserved.
