# Data Visualization

## Match the chart to the question
- Bar chart: compare categories.
- Histogram: inspect a numeric distribution.
- Box plot: compare spread and potential outliers.
- Scatter plot: inspect relationships between two numeric variables.
- Line chart: show ordered measurements, often over time.
- Heatmap: show a matrix such as correlations.
Avoid pie charts with many categories and 3D effects that distort comparisons.

## Good chart practice
Give the chart a descriptive title, label axes with units, use readable scales, show data source and time range, and make colors accessible. Avoid truncated axes when they exaggerate differences. Don't encode meaning with color alone.

## Matplotlib example
```python
import matplotlib.pyplot as plt
categories = ["A", "B", "C"]
values = [12, 19, 14]
fig, ax = plt.subplots()
ax.bar(categories, values)
ax.set(title="Values by category", xlabel="Category", ylabel="Count")
fig.tight_layout()
plt.show()
```

## Seaborn
Seaborn offers statistical plots built on Matplotlib. Use `histplot`, `boxplot`, `scatterplot`, `lineplot`, and `heatmap`. Always inspect the data type and aggregation before plotting.

## Reproducibility
Keep plotting code in scripts or notebooks, set random seeds for simulated data, and save final figures at suitable resolution. Visualization can reveal patterns but does not by itself establish causality.
