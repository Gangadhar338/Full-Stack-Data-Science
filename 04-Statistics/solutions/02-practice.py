import numpy as np

x = np.array([2, 3, 3, 4, 8, 20], dtype=float)
q1, q3 = np.quantile(x, [0.25, 0.75])
print("Mean:", x.mean())
print("Median:", np.median(x))
print("Range:", x.max() - x.min())
print("IQR:", q3 - q1)
print("Independent events:", 0.2 * 0.5)
