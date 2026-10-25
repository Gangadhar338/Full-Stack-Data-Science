import numpy as np
import pandas as pd

scores = np.array([72, 85, 91, 66, 85])
print("Mean:", round(float(scores.mean()), 2))
print("Above 80:", scores[scores > 80].tolist())

df = pd.DataFrame({
    "student": ["Asha", "Ravi", "Mina", "Dev"],
    "city": ["Hyderabad", "Vijayawada", "Hyderabad", "Vijayawada"],
    "score": [88, None, 93, 76],
})
print("Missing values:")
print(df.isna().sum())
df["score"] = df["score"].fillna(df["score"].median())
print("Average score by city:")
print(df.groupby("city")["score"].mean().round(2))
