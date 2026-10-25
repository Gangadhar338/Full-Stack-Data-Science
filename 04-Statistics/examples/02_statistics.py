import numpy as np

data = np.array([12, 13, 14, 14, 15, 16, 100], dtype=float)
print("Mean:", round(float(np.mean(data)), 2))
print("Median:", float(np.median(data)))
q1, q3 = np.quantile(data, [0.25, 0.75])
print("IQR:", round(float(q3 - q1), 2))
print("Sample standard deviation:", round(float(np.std(data, ddof=1)), 2))
