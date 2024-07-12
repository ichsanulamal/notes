### Constructing a Portfolio with Two Stocks

#### Portfolio Weights
- **xA**: Fraction of portfolio in Stock A
- **xB**: Fraction of portfolio in Stock B
- **Sum of weights**: \( xA + xB = 1 \)

#### Future Log Returns
- Log returns are considered random variables, taking different values with various probabilities.
- Index **i** represents possible future scenarios.

#### Expected Value (Mean) of Log Returns
- Denoted as **R**, the log return varies across scenarios with different probabilities.
- Expected log return is calculated as:
  \[
  \mathbb{E}[R] = \sum_i p_i R_i
  \]
  where \( p_i \) is the probability of scenario **i** and \( R_i \) is the return in scenario **i**.

#### Portfolio Returns
- Total return of the portfolio in each scenario:
  \[
  R_p = xA \cdot R_A + xB \cdot R_B
  \]
  where \( R_A \) and \( R_B \) are the returns of stocks A and B respectively.

#### Expected Value of Portfolio Return
- The expected value of the portfolio return is the weighted sum of the individual stock's expected returns:
  \[
  \mathbb{E}[R_p] = xA \cdot \mathbb{E}[R_A] + xB \cdot \mathbb{E}[R_B]
  \]
  - The summation distributes across the sum.
  - Weights can be pulled out since they are independent of scenarios.
  - Each term represents the expected value of the individual asset's return.

#### Portfolio Variance
- To calculate the variance of the portfolio return, consider:
  \[
  \text{Var}(R_p) = xA^2 \cdot \text{Var}(R_A) + xB^2 \cdot \text{Var}(R_B) + 2 \cdot xA \cdot xB \cdot \text{Cov}(R_A, R_B)
  \]
  where:
  - \( \text{Var}(R_A) \) and \( \text{Var}(R_B) \) are the variances of stocks A and B respectively.
  - \( \text{Cov}(R_A, R_B) \) is the covariance between the returns of stocks A and B.

By understanding these components, you can construct and analyze the mean and variance of a two-stock portfolio.