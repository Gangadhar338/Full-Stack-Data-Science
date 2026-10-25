from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent

CONTENT = {
"02-SQL": {
"lessons/02-core-concepts.md": r"""
# SQL Core Concepts — From Beginner to Practical

## 1. What SQL is
SQL (Structured Query Language) is used to define, read, change, and manage relational data. A table has columns (fields) and rows (records). A primary key uniquely identifies a row; a foreign key links rows between tables.

## 2. Create sample tables
```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 0),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

## 3. Read, filter, and sort
```sql
SELECT name, city
FROM customers
WHERE city = 'Hyderabad'
ORDER BY name;
```
`SELECT` chooses columns, `FROM` chooses a table, `WHERE` filters rows, and `ORDER BY` sorts results. Use `IS NULL` rather than `= NULL`.

## 4. Aggregation and grouping
```sql
SELECT customer_id, COUNT(*) AS order_count, SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```
`WHERE` filters rows before grouping; `HAVING` filters grouped results.

## 5. Joins
```sql
SELECT c.name, o.order_id, o.amount
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id;
```
`INNER JOIN` returns matching rows; `LEFT JOIN` keeps all left-side rows even when there is no match.

## 6. CTEs and window functions
```sql
WITH customer_totals AS (
    SELECT customer_id, SUM(amount) AS spend
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, spend,
       DENSE_RANK() OVER (ORDER BY spend DESC) AS spend_rank
FROM customer_totals;
```
A CTE (`WITH`) names a query for readability. Window functions calculate across related rows without collapsing them like `GROUP BY`.

## 7. Transactions and indexes
Use `BEGIN`, `COMMIT`, and `ROLLBACK` to group related changes safely. Index columns used frequently for joins or filters, but remember indexes consume storage and can slow writes. Confirm plans with your database's `EXPLAIN`.

## Common mistakes
- Joining tables on the wrong key, creating duplicate rows.
- Using `WHERE` for aggregate conditions instead of `HAVING`.
- Forgetting that NULL represents missing/unknown data.
- Using `SELECT *` in production queries when only a few columns are needed.

## Practice checklist
1. Return all customers from one city.
2. Find each customer's total spend.
3. Find customers with no orders using `LEFT JOIN`.
4. Rank customers by spend.
5. Explain when a transaction should be rolled back.
""",
"examples/02_customer_analytics.sql": r"""
-- Portable SQL example; run after creating the customers and orders tables
-- from lessons/02-core-concepts.md.
SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.amount), 0) AS total_spend
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.name;
""",
"exercises/02-sql-practice.md": r"""
# SQL Exercises

Use the `customers` and `orders` tables in `lessons/02-core-concepts.md`.

1. Select customer names in Hyderabad, alphabetically.
2. Return order count and total spend per customer, including customers with zero orders.
3. Find orders with amounts between 500 and 2000 inclusive.
4. Return customers whose total spend exceeds 1000.
5. Rank customers by total spend using a window function.
6. Explain the difference between `WHERE` and `HAVING`.
7. Write a query that finds customers with no orders.
""",
"solutions/02-sql-practice.sql": r"""
-- 1
SELECT name FROM customers WHERE city = 'Hyderabad' ORDER BY name;

-- 2
SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.amount), 0) AS total_spend
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name;

-- 3
SELECT * FROM orders WHERE amount BETWEEN 500 AND 2000;

-- 4
SELECT c.customer_id, c.name, SUM(o.amount) AS total_spend
FROM customers c JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 1000;

-- 5
WITH totals AS (
  SELECT customer_id, SUM(amount) AS total_spend
  FROM orders GROUP BY customer_id
)
SELECT customer_id, total_spend,
       DENSE_RANK() OVER (ORDER BY total_spend DESC) AS spend_rank
FROM totals;

-- 7
SELECT c.customer_id, c.name
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;
"""
},
"03-NumPy-Pandas": {
"lessons/02-core-concepts.md": r"""
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
""",
"examples/02_numpy_pandas.py": r"""
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
""",
"exercises/02-practice.md": r"""
# NumPy and Pandas Exercises

1. Make a NumPy array from 10 values and calculate mean, median, and standard deviation.
2. Build a DataFrame with at least 5 rows and 3 columns.
3. Count missing values per column.
4. Fill missing numeric values using a justified strategy.
5. Remove exact duplicate rows and report how many were removed.
6. Group records by category and calculate count, mean, and sum.
7. Merge two DataFrames and validate the expected relationship.
8. Save the cleaned table as CSV.
""",
"solutions/02-practice.py": r"""
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
"""
},
"04-Statistics": {
"lessons/02-core-concepts.md": r"""
# Statistics and Probability for Data Science

## Population, sample, and variables
A population is the full group of interest; a sample is the observed subset. A parameter describes a population and a statistic describes a sample. Variables may be numeric or categorical.

## Descriptive statistics
- Mean: sum divided by count; sensitive to extreme values.
- Median: middle sorted value; more robust to outliers.
- Mode: most frequent value.
- Range: maximum minus minimum.
- Variance: average squared deviation (sample variance uses an `n-1` denominator).
- Standard deviation: square root of variance.
- Quantiles/IQR: describe spread; IQR = Q3 - Q1.

## Probability
Probability ranges from 0 to 1. For independent events, `P(A and B) = P(A)P(B)`. Conditional probability is `P(A|B) = P(A and B)/P(B)` when `P(B)>0`. Independence and mutual exclusivity are not the same.

## Distributions
The normal distribution is symmetric and described by mean and standard deviation. The binomial distribution counts successes in a fixed number of independent trials with constant success probability. Real data need not be normally distributed.

## Sampling and confidence intervals
Sampling variability means estimates change from sample to sample. A confidence interval procedure has a long-run coverage interpretation; a 95% confidence interval is not a 95% probability that a fixed parameter lies inside this already-computed interval.

## Hypothesis tests
State a null hypothesis and alternative, choose a test based on design and assumptions, calculate a test statistic and p-value, and report effect size and uncertainty. A p-value is not the probability that the null hypothesis is true. Statistical significance does not guarantee practical importance.

## Correlation and causation
Correlation measures association, not proof of causality. Confounding, selection bias, reverse causality, and measurement errors can mislead.

## Practice
Explain mean versus median for skewed data; calculate IQR; distinguish independent from mutually exclusive events; interpret a confidence interval and p-value in plain language.
""",
"examples/02_statistics.py": r"""
import numpy as np

data = np.array([12, 13, 14, 14, 15, 16, 100], dtype=float)
print("Mean:", round(float(np.mean(data)), 2))
print("Median:", float(np.median(data)))
q1, q3 = np.quantile(data, [0.25, 0.75])
print("IQR:", round(float(q3 - q1), 2))
print("Sample standard deviation:", round(float(np.std(data, ddof=1)), 2))
""",
"exercises/02-practice.md": r"""
# Statistics Exercises

1. Compute mean, median, range, and IQR for [2, 3, 3, 4, 8, 20].
2. Explain why median can be preferable for income data.
3. If events A and B are independent, P(A)=0.2 and P(B)=0.5; calculate P(A and B).
4. Explain a 95% confidence interval without saying there is a 95% chance the fixed parameter is in this one interval.
5. Explain why a small p-value does not measure effect size.
6. Give an example of confounding in an observational dataset.
""",
"solutions/02-practice.py": r"""
import numpy as np

x = np.array([2, 3, 3, 4, 8, 20], dtype=float)
q1, q3 = np.quantile(x, [0.25, 0.75])
print("Mean:", x.mean())
print("Median:", np.median(x))
print("Range:", x.max() - x.min())
print("IQR:", q3 - q1)
print("Independent events:", 0.2 * 0.5)
"""
},
"05-Data-Visualization": {
"lessons/02-core-concepts.md": r"""
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
""",
"examples/02_visualization.py": r"""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 135, 180]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(months, sales, marker="o")
ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (units)")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig("monthly_sales.png", dpi=150)
print("Saved monthly_sales.png")
""",
"exercises/02-practice.md": r"""
# Visualization Exercises

1. Plot category counts as a bar chart.
2. Plot a numeric distribution as a histogram.
3. Compare two groups with a box plot.
4. Plot two numeric columns in a scatter plot.
5. Add a title, axis labels, units, and a source note.
6. Explain why a line chart is usually appropriate for time-ordered data but not unordered categories.
"""
},
"06-EDA": {
"lessons/02-core-concepts.md": r"""
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
""",
"examples/02_eda.py": r"""
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
""",
"exercises/02-practice.md": r"""
# EDA Exercises

1. Write five questions to ask before analysing a dataset.
2. Build a data-quality report with types, missing values, duplicates, and ranges.
3. Investigate a possible outlier without immediately deleting it.
4. Identify a possible source of target leakage in a churn dataset.
5. Produce three charts that answer different analytical questions.
6. Write a one-page report with findings and limitations.
"""
},
"07-Machine-Learning": {
"lessons/03-supervised-learning.md": r"""
# Supervised Machine Learning

## Problem types
Regression predicts a numeric target. Classification predicts a class or class probability. Unsupervised learning explores structure without a labelled target.

## Workflow
1. Define target, prediction time, success metric, and baseline.
2. Split training and test data before fitting transformations.
3. Build preprocessing and model steps in a pipeline.
4. Tune only using training data and cross-validation.
5. Evaluate once on a held-out test set.
6. Inspect errors, fairness, robustness, and deployment constraints.

## Common algorithms
- Linear/logistic regression: interpretable baselines with assumptions and regularization.
- Decision tree: nonlinear rules, but can overfit.
- Random forest: ensemble of trees, often robust.
- Gradient boosting: sequentially improves errors; tune carefully.
- k-nearest neighbors: distance-based and sensitive to scaling.
- Clustering: groups observations without labels; validate usefulness rather than assuming clusters are true categories.

## Metrics
Classification: confusion matrix, precision, recall, F1, ROC-AUC; accuracy can mislead on imbalanced classes. Regression: MAE, RMSE, and R-squared. Choose metrics based on the cost of errors.

## Leakage and reproducibility
Never fit scalers or imputers on test data. Use a `Pipeline` and `ColumnTransformer`. Record random seeds, versions, dataset provenance, and the final metric.

## Practice
Explain train/validation/test roles, choose metrics for rare fraud, compare a baseline to a tree model, and inspect false negatives.
""",
"examples/03_classification_pipeline.py": r"""
# Install scikit-learn to run: python -m pip install scikit-learn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions), 3))
print(classification_report(y_test, predictions))
""",
"exercises/03-practice.md": r"""
# Machine Learning Exercises

1. Explain regression versus classification.
2. Split a dataset into train and test subsets with a fixed seed.
3. Build a baseline model and record its metric.
4. Put preprocessing and the model in one pipeline.
5. For an imbalanced fraud dataset, explain why accuracy alone may be misleading.
6. Identify two possible leakage sources.
7. Compare model errors and discuss the real-world cost of false positives and false negatives.
""",
"solutions/03-practice.md": r"""
# Machine Learning Exercise Guidance

1. Regression predicts numeric quantities; classification predicts categories.
2. Use `train_test_split(..., random_state=42, stratify=y)` for independent labelled samples.
3. Compare against a simple baseline such as majority-class prediction or predicting the training median.
4. Use `Pipeline` and `ColumnTransformer` so preprocessing is fitted only on training folds.
5. A model can obtain high accuracy by predicting the majority class while missing almost every fraud case; inspect precision, recall, F1, and the confusion matrix.
6. Examples: using a post-outcome field, fitting imputation/scaling on all rows before splitting, or random splitting time-ordered data.
"""
},
"08-Deep-Learning": {
"lessons/02-core-concepts.md": r"""
# Deep Learning Fundamentals

## Neural networks
A neural network applies linear transformations and nonlinear activation functions in layers. Training adjusts weights to reduce a loss function. Backpropagation computes gradients; an optimizer uses them to update parameters.

## Core terms
- Feature/input: information supplied to the model.
- Logits: raw model scores before a probability transform.
- Loss: numeric objective minimized during training.
- Epoch: one pass through training data.
- Batch: subset used for one parameter update.
- Learning rate: size of optimizer updates.
- Overfitting: training performance improves while generalization does not.

## Training loop
Prepare data, normalize inputs when appropriate, define model and loss, train on batches, validate after epochs, use early stopping where justified, and evaluate on a test set only after choices are finalized.

## Common architectures
CNNs are often used for spatial/image patterns; RNNs and LSTMs process sequences; transformers use attention and are widely used for language, vision, and multimodal tasks. Architecture choice depends on the task and available data.

## Responsible practice
Track experiments, random seeds, compute cost, dataset permissions, and model limitations. Deep learning is not automatically better than a simpler baseline.
""",
"examples/02_torch_regression.py": r"""
# Install PyTorch for your platform using https://pytorch.org/get-started/locally/
import torch
from torch import nn

torch.manual_seed(42)
X = torch.arange(0, 10, dtype=torch.float32).reshape(-1, 1)
y = 2 * X + 1
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for epoch in range(500):
    prediction = model(X)
    loss = loss_fn(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Learned weight and bias:", model.weight.item(), model.bias.item())
print("Final loss:", round(loss.item(), 4))
""",
"exercises/02-practice.md": r"""
# Deep Learning Exercises

1. Explain a neuron, activation, loss, and gradient.
2. Draw the flow of a forward pass and backward pass.
3. Train the simple regression example and record final loss.
4. Change the learning rate and observe convergence.
5. Explain why validation data is separate from training data.
6. Describe two ways to reduce overfitting.
"""
},
"09-NLP-and-Generative-AI": {
"lessons/03-llms-and-rag.md": r"""
# NLP, LLMs, Embeddings, and RAG

## NLP and tokenization
Natural Language Processing handles text tasks such as classification, extraction, summarization, translation, and question answering. A tokenizer converts text into tokens; tokens are not always whole words.

## Transformers and LLMs
Transformers use attention to combine contextual information. Large language models generate token sequences based on learned patterns and the provided context. They can produce incorrect or fabricated claims, so important outputs need verification.

## Embeddings and vector search
An embedding maps text to a numeric vector so semantically related text may be close in vector space. Retrieval systems search for relevant chunks using similarity and sometimes metadata filters. Similarity is a ranking signal, not proof of truth.

## Retrieval-Augmented Generation (RAG)
1. Load permitted documents.
2. Extract and normalize text.
3. Split text into chunks while preserving useful context.
4. Embed chunks and store vectors with source metadata.
5. Retrieve relevant chunks for a question.
6. Generate an answer grounded in retrieved context.
7. Cite sources and evaluate retrieval and answer quality.

## RAG risks and safeguards
Watch for bad chunking, stale documents, poor retrieval, prompt injection inside retrieved documents, privacy leaks, unsupported answers, and missing citations. Treat document content as untrusted data, separate instructions from evidence, restrict tools, and test adversarial cases.

## Evaluation
Evaluate retrieval recall/precision, groundedness, citation correctness, answer usefulness, latency, and cost. Use a fixed evaluation set and human review for high-impact tasks.
""",
"examples/03_rag_baseline.py": r"""
# Minimal retrieval baseline using keyword overlap; no external packages needed.
# This demonstrates the RAG stages, not a production embedding search system.
documents = [
    {"source": "python.md", "text": "Python lists are ordered mutable collections."},
    {"source": "sql.md", "text": "SQL joins combine rows from related tables."},
    {"source": "ml.md", "text": "Train test splits estimate generalization on held-out data."},
]

def retrieve(question, docs, top_k=2):
    terms = set(question.lower().split())
    ranked = []
    for doc in docs:
        words = set(doc["text"].lower().replace(".", "").split())
        score = len(terms & words)
        ranked.append((score, doc))
    return [doc for score, doc in sorted(ranked, key=lambda item: item[0], reverse=True)[:top_k] if score > 0]

question = "How do SQL joins combine tables?"
results = retrieve(question, documents)
for item in results:
    print(f"[{item['source']}] {item['text']}")
if not results:
    print("No supporting document found; do not invent an answer.")
""",
"exercises/03-practice.md": r"""
# Generative AI Exercises

1. Explain tokens, embeddings, context windows, and hallucinations.
2. Draw the stages of a RAG pipeline.
3. Create 10 questions with expected source documents and expected answers.
4. Compare keyword retrieval with embedding retrieval.
5. Explain why retrieved documents must be treated as untrusted input.
6. Design a test for unsupported questions and missing citations.
7. Record latency, cost, retrieval quality, and answer quality.
""",
"solutions/03-practice.md": r"""
# GenAI Exercise Guidance

A sound RAG system separates retrieval from generation, preserves document provenance, returns citations, and abstains when evidence is insufficient. Evaluate retrieval and generated answers separately. Do not assume that a fluent answer is correct. The included keyword baseline is educational and should be replaced by a tested embedding model and vector store for a real application.
"""
},
"10-FastAPI": {
"lessons/02-building-apis.md": r"""
# FastAPI — Building and Testing APIs

## API basics
An API exposes operations over a defined interface. REST APIs commonly use HTTP methods: GET reads, POST creates or triggers processing, PUT replaces, PATCH partially updates, and DELETE removes. Use appropriate status codes and validate request data.

## FastAPI concepts
FastAPI uses Python type annotations and Pydantic models to validate request bodies. It generates OpenAPI documentation automatically. Keep route handlers small and move business logic into testable functions or service modules.

## Reliability and security
Validate inputs, avoid exposing stack traces or secrets, configure CORS narrowly, use authentication and authorization when needed, set request limits, log safely, and manage errors consistently. Do not place API keys in source control.

## Run
Install with `python -m pip install fastapi uvicorn`. Save the example as `examples/02_main.py`, then run `python -m uvicorn examples.02_main:app --reload` if the examples directory is importable as a package; alternatively run from the examples directory with `uvicorn 02_main:app --reload`.

## Testing
Use FastAPI's `TestClient` to test successful responses, invalid requests, and error conditions. Add integration tests for database or model dependencies.
""",
"examples/02_main.py": r"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Data Science Course API", version="1.0.0")

class PredictionRequest(BaseModel):
    hours_studied: float = Field(ge=0, le=24)

class PredictionResponse(BaseModel):
    estimated_score: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    score = min(100.0, max(0.0, 40.0 + 2.5 * request.hours_studied))
    return PredictionResponse(estimated_score=round(score, 2))
""",
"exercises/02-practice.md": r"""
# FastAPI Exercises

1. Add a `/version` endpoint.
2. Add a Pydantic request model with validation.
3. Return a 422 response for invalid input.
4. Add tests for health and prediction endpoints.
5. Explain the difference between authentication and authorization.
6. Move prediction logic into a separate function and test it independently.
""",
"solutions/02-test_api.py": r"""
# Install: python -m pip install fastapi httpx
from fastapi.testclient import TestClient
from examples_02_main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict():
    response = client.post("/predict", json={"hours_studied": 4})
    assert response.status_code == 200
    assert response.json()["estimated_score"] == 50.0

def test_invalid_input():
    response = client.post("/predict", json={"hours_studied": 30})
    assert response.status_code == 422
"""
},
"11-Streamlit-Dashboards": {
"lessons/02-building-dashboards.md": r"""
# Streamlit Dashboards

## App structure
Streamlit turns a Python script into an interactive web app. Widgets return user selections; Streamlit reruns the script when a widget changes. Use caching for expensive deterministic work, not for user-specific secrets.

## Dashboard workflow
1. Define the audience and decisions the dashboard supports.
2. Load and validate data.
3. Add filters and meaningful summary metrics.
4. Visualize trends and comparisons.
5. Explain missing data and limitations.
6. Test empty selections, invalid uploads, and large inputs.

## Good practice
Use clear labels, avoid misleading axes, display units and date ranges, and separate raw data from calculated metrics. Do not upload sensitive data without permission. Keep secrets in environment variables or Streamlit secrets rather than source files.

## Run
Install with `python -m pip install streamlit pandas`. Save the example and run `streamlit run examples/02_dashboard.py`.
""",
"examples/02_dashboard.py": r"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")
data = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "region": ["North", "South", "North", "South"],
    "sales": [1200, 950, 1450, 1300],
})
regions = st.multiselect("Region", sorted(data["region"].unique()), default=sorted(data["region"].unique()))
filtered = data[data["region"].isin(regions)]
st.metric("Total sales", f"{filtered['sales'].sum():,.0f}")
st.dataframe(filtered, use_container_width=True)
if not filtered.empty:
    st.bar_chart(filtered.set_index("month")["sales"])
else:
    st.info("Select at least one region to view data.")
""",
"exercises/02-practice.md": r"""
# Streamlit Exercises

1. Add a date or category filter.
2. Display total, average, and record count.
3. Add a chart that answers a real business question.
4. Handle the case where filters return zero rows.
5. Add CSV upload with validation and a maximum-size policy.
6. Explain when caching is appropriate and when it is not.
"""
},
"12-Deployment-and-Docker": {
"lessons/02-deployment-basics.md": r"""
# Deployment, Docker, and MLOps Fundamentals

## Deployment concepts
A local script, API, and dashboard have different runtime needs. Deployment makes an application available in a target environment with reproducible dependencies, configuration, monitoring, and rollback procedures.

## Docker
A Docker image packages an application and its runtime dependencies. A container is a running instance of an image. Keep images small, use a suitable base image, pin dependencies where practical, use non-root users, and never bake secrets into images.

## Environment configuration
Use environment variables for deployment-specific settings. Keep `.env` files containing secrets out of Git. Provide a `.env.example` with placeholder variable names, not real credentials.

## CI and observability
Automated checks should run tests and static checks on changes. Monitor availability, latency, errors, resource use, and model/data drift where relevant. Logs should avoid passwords, API keys, and unnecessary personal data.

## MLOps
Track dataset versions, model artifacts, metrics, configuration, and experiment parameters. Define a rollback plan and test model behavior after deployment. A successful container build alone does not prove the application is correct or secure.
""",
"examples/02_Dockerfile": r"""
# Example for a simple Python web service; adjust module and dependency names to your app.
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
""",
"exercises/02-practice.md": r"""
# Deployment Exercises

1. Write a `requirements.txt` for a small API.
2. Create a Dockerfile and explain each instruction.
3. Create `.env.example` without real secrets.
4. Add a test step to a CI workflow.
5. Explain image versus container.
6. Design a health check and rollback plan.
7. List the metrics to monitor after deployment.
"""
},
"13-End-to-End-Projects": {
"lessons/02-project-delivery-checklist.md": r"""
# End-to-End Data Science Project Delivery Checklist

Every project should include a clear problem statement, intended user, data source and license, data dictionary, setup instructions, reproducible pipeline, baseline, evaluation metrics, limitations, tests, and a demonstration.

## Suggested project sequence
1. Sales analysis dashboard: clean data, EDA, charts, filters, and a business summary.
2. House-price regression: leakage-safe split, baseline, pipeline, MAE/RMSE, error analysis.
3. Customer churn classification: imbalance-aware metrics, threshold choice, model explanation, and limitations.
4. Model prediction API: input validation, health route, tests, logging, and container.
5. Document Q&A with RAG: permitted documents, chunking, retrieval evaluation, grounded answers, citations, and abstention.

## Definition of done
- A new user can follow the README from a clean environment.
- Commands are tested on the stated Python version.
- Data provenance and licensing are documented.
- No credentials or private data are committed.
- Tests cover important behavior and edge cases.
- Results include metrics and limitations rather than unsupported claims.
- The project can be reproduced and its known failures are documented.
""",
"exercises/02-project-review.md": r"""
# Project Review Exercises

For each project, submit:
1. Problem statement and intended audience.
2. Data dictionary and data provenance.
3. Reproducible setup and run commands.
4. Baseline and chosen metric with justification.
5. Tests and edge cases.
6. Screenshots or sample API requests/responses.
7. Limitations, risks, and next steps.
"""
},
"14-Exercises": {
"lessons/02-how-to-practice.md": r"""
# How to Practise Data Science Effectively

For each topic, first explain the concept in your own words, then run a minimal example, change one input, predict the result, execute it, and explain any difference. Keep a record of mistakes and their fixes.

## Practice tiers
- Beginner: reproduce a small example and explain each line.
- Intermediate: adapt it to a new dataset or requirement.
- Advanced: test edge cases, compare approaches, measure performance, and document trade-offs.

Do not copy a solution before attempting the problem. When checking a solution, compare reasoning and tests, not just the final output.
""",
"exercises/02-mixed-practice.md": r"""
# Mixed Data Science Practice

1. Python: count word frequencies in a text file.
2. SQL: find top customers by spend.
3. Pandas: clean missing and duplicated records.
4. Statistics: compare mean and median for skewed data.
5. Visualization: show a time trend with labelled axes.
6. EDA: write three findings and two limitations.
7. ML: build a baseline and evaluate a held-out set.
8. GenAI: design a RAG evaluation set and test unsupported questions.
9. API: validate a request and test an invalid value.
10. Deployment: explain how to keep secrets out of source control.
"""
},
"15-Interview-Preparation": {
"lessons/02-interview-method.md": r"""
# Data Science Interview Preparation

## Answer structure
For conceptual questions: define the idea, explain why it matters, give a small example, name a limitation, and state when you would use it. For coding questions: clarify requirements, discuss edge cases, write a simple solution, test it, then improve it.

## Topics to review
- Python: mutability, comprehensions, generators, exceptions, complexity.
- SQL: joins, aggregation, CTEs, window functions, NULL semantics.
- Statistics: sampling, confidence intervals, p-values, bias, correlation.
- ML: leakage, cross-validation, regularization, metrics, drift.
- GenAI: tokens, embeddings, RAG, hallucinations, evaluation, security.
- Engineering: APIs, tests, containers, secrets, logs, monitoring.

## Portfolio discussion
Be ready to explain your own contribution, the baseline, why the metric fits the problem, failed experiments, data limitations, reproducibility, and what you would improve. Never claim a project or result you did not actually build or measure.
""",
"exercises/02-interview-questions.md": r"""
# Interview Questions

1. Why can a high-accuracy model be poor on an imbalanced dataset?
2. Explain data leakage with a concrete example.
3. What is the difference between a primary key and a foreign key?
4. When would you use a median instead of a mean?
5. What does a confidence interval communicate?
6. How does a train/test split differ from cross-validation?
7. What are embeddings and how does RAG use them?
8. How do you evaluate whether RAG answers are grounded?
9. How do you test an API endpoint?
10. How would you protect secrets in a deployed app?
"""
}
}

def write_if_missing(relative_path, content):
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print("KEPT existing:", relative_path)
        return False
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
    print("CREATED:", relative_path)
    return True

def main():
    created = 0
    for module, files in CONTENT.items():
        for relative, body in files.items():
            created += write_if_missing(Path(module) / relative, body)
    # Add an honest progress guide at the root without overwriting the existing README.
    guide = ROOT / "COURSE_COMPLETION_TRACKER.md"
    if not guide.exists():
        guide.write_text("""# Course Completion Tracker

This repository is a learning project under active development. A generated file or passing structural test does not by itself mean a topic is complete.

For each module, verify:
- [ ] Theory reviewed for correctness and clarity
- [ ] Example code executed in a clean environment
- [ ] Exercises attempted independently
- [ ] Solutions checked and explained
- [ ] Automated tests cover key behavior and edge cases
- [ ] Dependencies and run instructions verified
- [ ] Data sources and licenses documented where relevant
- [ ] Limitations and security considerations documented

The content-expansion script adds lesson material and starter examples. It deliberately preserves existing files. Some examples require optional libraries; install the dependency noted in the example before running it.
""", encoding="utf-8")
        created += 1
        print("CREATED: COURSE_COMPLETION_TRACKER.md")
    print(f"\nExpansion complete. Created {created} new files; existing files were preserved.")
    print("Run: python -m unittest discover -s tests -v")
    print("Note: optional-dependency examples may require package installation and manual execution.")

if __name__ == "__main__":
    main()
