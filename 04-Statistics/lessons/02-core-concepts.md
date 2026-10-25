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
