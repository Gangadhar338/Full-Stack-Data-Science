import pandas as pd

df = pd.DataFrame({
    "region": ["North", "South", "North", "South", "North"],
    "sales": [120, 95, None, 110, 500],
    "units": [3, 2, 4, 3, 12],
})
print("Shape:", df.shape)
print("\nTypes:")
print(df.dtypes)
print("\nMissing:")
print(df.isna().sum())
print("\nDuplicates:", int(df.duplicated().sum()))
print("\nSummary:")
print(df.describe(include="all"))
print("\nSales by region:")
print(df.groupby("region")["sales"].agg(["count", "mean", "median", "max"]))
