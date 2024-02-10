The t-distribution, also known as Student's t-distribution, is a probability distribution that is used in statistics. It is similar to the standard normal distribution (bell curve), but it has heavier tails, which means it is more spread out and has more probability in the tails of the distribution compared to the normal distribution.

The t-distribution is commonly used in hypothesis testing and confidence interval estimation when the sample size is small and the population standard deviation is unknown. It arises from the fact that when we estimate the population standard deviation from a sample, there is additional uncertainty introduced into the calculations.

The shape of the t-distribution depends on a parameter called the degrees of freedom (\( \nu \)). The degrees of freedom represent the number of independent observations in a sample. As the degrees of freedom increase, the t-distribution approaches the standard normal distribution. When the degrees of freedom are small, the tails of the t-distribution are thicker, indicating greater uncertainty.

The t-distribution is symmetrical and centered at zero, like the standard normal distribution, and its shape becomes more similar to the normal distribution as the degrees of freedom increase. It is often used in hypothesis testing, especially when dealing with small sample sizes or when the population standard deviation is unknown.

The probability density function (PDF) of the t-distribution is given by:

\[ f(t) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\pi \nu} \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu + 1}{2}} \]

where:
- \( t \) is the random variable following the t-distribution.
- \( \nu \) is the degrees of freedom.
- \( \Gamma \) is the gamma function.

The t-distribution is widely used in various statistical analyses, particularly in situations where assumptions about normality and sample size need to be carefully considered.