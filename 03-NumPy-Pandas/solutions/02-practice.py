import pandas as pd

df = pd.DataFrame({
    "category": ["A", "A", "B", "B", "B"],
    "value": [10, None, 30, 40, 40],
})
print("Missing:", df.isna().sum().to_dict())
df["value"] = df["value"].fillna(df["value"].median())
before = len(df)
df = df.drop_duplicates()
print("Duplicates removed:", before - len(df))
print(df.groupby("category")["value"].agg(["count", "mean", "sum"]))
df.to_csv("cleaned_practice.csv", index=False)
