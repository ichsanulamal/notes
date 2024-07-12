# Calculating Portfolio Risk: Variance and Volatility

### Understanding Variance for One Asset
- **Variance Formula**:
  \[
  \sigma^2 = \sum (x_i - \mu)^2 \times P(x_i)
  \]
  - \(x_i\): Each observation
  - \(\mu\): Mean of the observations
  - \(P(x_i)\): Probability of each observation

- This formula generalizes the familiar variance formula:
  \[
  \sigma^2 = \frac{\sum (x_i - \mu)^2}{n}
  \]
  - Assumes equal probability for each observation.

### Portfolio Variance
- **Formula**:
  \[
  \sigma_p^2 = \sum w_i^2 \sigma_i^2 + \sum \sum w_i w_j \sigma_i \sigma_j \rho_{ij}
  \]
  - \(w_i\): Weight of asset \(i\)
  - \(\sigma_i^2\): Variance of asset \(i\)
  - \(\rho_{ij}\): Correlation between assets \(i\) and \(j\)

- **Covariance** (\(\sigma_{ij}\)):
  \[
  \sigma_{ij} = \rho_{ij} \sigma_i \sigma_j
  \]
  - Measures joint variability of two assets.
  - Positive covariance: Both assets move in the same direction.

### Importance of Covariance
- **Diversification Benefit**:
  - Covariance underpins the benefits of diversification.
  - Lower covariance between assets reduces portfolio risk.

### Portfolio Variance with Correlation
- **Correlation Coefficient (\(\rho_{ij}\))**:
  - Range: \([-1, 1]\)
  - \(\rho_{ij} = 1\): Assets are perfectly correlated.
  - \(\rho_{ij} = -1\): Assets are perfectly anti-correlated.

- **Impact on Portfolio Variance**:
  - \(\rho_{ij} = 1\):
    \[
    \sigma_p = \sum w_i \sigma_i
    \]
    - Portfolio standard deviation is a weighted average of individual standard deviations.
  
  - \(\rho_{ij} < 1\):
    - Portfolio standard deviation is less than the weighted average of individual standard deviations.
  
  - \(\rho_{ij} = -1\):
    \[
    \sigma_p = \left| \sum w_i \sigma_i \right|
    \]
    - Portfolio variance can be reduced to zero if perfectly hedged.

### Practical Implications
- **Perfect Hedging**:
  - Weights for hedging:
    \[
    w_A = \frac{\sigma_B}{\sigma_A + \sigma_B}
    \]
  - Perfect hedging is theoretical due to systematic risk.

By understanding and applying these concepts, we can effectively measure and manage the risk in a portfolio.