# Machine Learning Exercise Guidance

1. Regression predicts numeric quantities; classification predicts categories.
2. Use `train_test_split(..., random_state=42, stratify=y)` for independent labelled samples.
3. Compare against a simple baseline such as majority-class prediction or predicting the training median.
4. Use `Pipeline` and `ColumnTransformer` so preprocessing is fitted only on training folds.
5. A model can obtain high accuracy by predicting the majority class while missing almost every fraud case; inspect precision, recall, F1, and the confusion matrix.
6. Examples: using a post-outcome field, fitting imputation/scaling on all rows before splitting, or random splitting time-ordered data.
