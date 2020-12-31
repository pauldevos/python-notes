## Linear Algebra

## Machine Learning Models (ideas)

1. Linear Regression (Ridge, Lasso)
2. Generalized Linear Models (Logistic Regression, Multinomial Regression, Ordinal Regression, Poisson Regression)
3. Generalized Additive Models
4. Decision Trees | Bagging | Random Forest | Boosting
5. Support Vector Machine
6. Clustering (K-Means, Hierarchical)
7. K-Nearest Neighbor
8. Dimensionality Reduction (Principal Component Analysis, Exploratory Factor Analysis, Non-Negative Matrix Factorization, Multi-Dimensional Scaling)
9. Association Rule Mining (Apriori Algorithm)
10. Text Mining
11. Hypothesis Testing
12. Design of Experiment
13. A/B Testing
14. Optimization (Linear Programming, Integer Programming, Mixed Integer Programming)

## Random Forests

- There are two ways to measure the quality of a split:
  - **Gini Impurity** and **Entropy**. They essentially measure the impurity and give similar results. `Scikit-learn` uses `gini index` by default but you can change it to entropy using criterion parameter.
- **Gini Impurity** - is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the subset. It basically means that `impurity increases with randomness`. For instance, let’s say we have a box with ten balls in it. If all the balls are same color, we have no randomness and impurity is zero. However, if we have 5 blue balls and 5 red balls, impurity is

#### Entropy and Information Gain

- **Entropy** is a `measure of uncertainty or randomness`. The more randomness a variable has, the higher the entropy is. The variables with uniform distribution have the highest entropy. For example, rolling a fair dice has 6 possible outcomes with equal probabilities so it has a uniform distribution and high entropy.

When choosing a feature to split, decision tree algorithm tries to achieve

- More predictiveness
- Less impurity (1 => 0)
- Lower entropy (1 => 0)
