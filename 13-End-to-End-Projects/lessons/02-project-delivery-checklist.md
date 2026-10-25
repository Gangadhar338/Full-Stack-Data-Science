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
