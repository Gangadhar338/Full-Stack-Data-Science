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
