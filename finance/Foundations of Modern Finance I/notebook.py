# Jupyter Notebook version of the R Markdown notebook

# ---
# title: "Testing the Random Walk"
# author: "Paul F. Mende"
# date: "Summer 2021"
# output: 
#   html_notebook:
#   df_print: paged
#   toc: yes
# ---

# ## Preliminaries

# Before we get started, let's install a few **packages**.
# - The `pip install` command is run **once** to download the software to your computer.
# - The `import` command is run **one time per session** in order to load a package's functions and make them available.

# In[1]:
# If you have never installed them, uncomment the lines below and run it one time.

# !pip install yfinance pandas numpy matplotlib

# In[2]:
# Now we'll load packages.

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ## Tootsie Roll

# Let's load some data and look at default summary stats for data from Tootsie Roll (TR).

# **Technical note:** Data is often exchanged using "flat files," which are plain text files that can be read using a simple text editor.

# In[3]:
# Fetch some test data from Yahoo! Finance

# Define query parameters
ticker = "TR"
date_first = "1987-12-31"
date_last = "2017-12-31"

# Get the data
TR = yf.download(ticker, start=date_first, end=date_last)

# In[4]:
# Here is what the price looks like over time

plt.plot(TR.index, TR['Adj Close'], label='Adjusted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('TR Adjusted Price 1988-2017')
plt.grid(True)
plt.show()

# In[5]:
# Compute the returns
P = TR['Adj Close']
r = np.diff(np.log(P))
N = len(r)

# The returns can also be stored as a new column in TR.
TR['r'] = np.append([np.nan], r)

# Trim off the first row, which has return NA
TR = TR.dropna()

plt.plot(TR.index, TR['r'], label='Daily Returns')
plt.xlabel('Time')
plt.ylabel('Returns')
plt.title('TR Daily Returns 1988-2017')
plt.grid(True)
plt.show()

# In[6]:
# The daily return series is noisy, and the mean value is barely visible.
# Compare the graph above with the simulation below, in which simulated returns have the same average volatility and zero mean.

plt.plot(TR.index, np.random.normal(scale=np.std(TR['r']), size=len(TR)), label='White Noise')
plt.ylim(-0.18, 0.18)
plt.xlabel('Time')
plt.ylabel('Returns')
plt.title('White Noise Process with TR Volatility')
plt.grid(True)
plt.show()

# ## Summary statistics and return distribution

# In[7]:
# These are high-level summary stats that pandas provides for any data frame.
TR.describe()

# In[8]:
# Annualization conventions
# Annualized return = 252 * (Daily return)
# Annualized std. dev. = sqrt(252) * (Daily std. dev)

mean_return_annualized = np.mean(r) * 252
volatility_annualized = np.std(r) * np.sqrt(252)

mean_return_annualized, volatility_annualized

# In[9]:
# The histogram of returns has fat tails (and therefore a thin middle).

plt.hist(r, bins=50)
plt.title('Histogram of TR Daily Returns')
plt.show()

# ## Lo & MacKinlay

# In[10]:
# Following Lo & MacKinlay, we ask whether the measured sample variance of returns grows linearly as a function of the observation interval.

Variance = [np.var(np.diff(np.log(P)))]

for n in range(2, 101):
    Variance.append(np.var(np.diff(np.log(P[::n]))))

plt.plot(Variance)
plt.xlabel('n')
plt.title('Variance of Returns From n-day Observations')
plt.grid(True)
plt.show()

# ## Variance and Ratios

# In[11]:
# Define functions for $\widehat \sigma^2_c$

def variance_c(X, q):
    T = len(X) - 1
    mu = (X[-1] - X[0]) / T
    m = (T - q) * (T - q + 1) * q / T
    sumsq = sum((X[t + 1] - X[t - q + 1] - q * mu) ** 2 for t in range(q, T))
    return sumsq / m

def z_stat(X, q):
    T = len(X) - 1
    c = np.sqrt(T * (3 * q) / (2 * (2 * q - 1) * (q - 1)))
    M = variance_c(X, q) / variance_c(X, 1) - 1
    return c * M

Vc = [variance_c(np.log(P), q) for q in range(1, 101)]
zstats = [z_stat(np.log(P), q) for q in range(2, 101)]
pValues = [2 * (1 - np.abs(np.random.normal(0, 1))) for z in zstats]

plt.bar(range(2, 101), zstats)
plt.xlabel('q')
plt.ylabel('z')
plt.title('z Statistics of Variance Ratio Test')
plt.show()

# ## Interpreting the test statistics

# In[12]:
# The test statistic $z(q)$ was constructed to be normally distributed as ${\cal N}(0,1)$ if the data followed a random walk and scaled accordingly.

sigma = [np.sqrt(252) * np.std(np.diff(np.log(P)))]
for n in range(2, 101):
    sigma.append(np.sqrt(252 / n) * np.std(np.diff(np.log(P[::n]))))

plt.bar(range(1, 101), sigma)
plt.xlabel('n')
plt.ylabel('Standard Deviation (annualized) / sqrt(n)')
plt.title('Volatility Scaling of Returns From n-day Observations (TR)')
plt.grid(True)
plt.show()

# In[13]:
# Simulation of returns with similar volatility

P_MC = np.exp(np.cumsum(np.random.normal(scale=0.02, size=N)))
sigma_MC = [np.sqrt(252) * np.std(np.diff(np.log(P_MC)))]

for n in range(2, 101):
    sigma_MC.append(np.sqrt(252 / n) * np.std(np.diff(np.log(P_MC[::n]))))

plt.bar(range(1, 101), sigma_MC)
plt.xlabel('n')
plt.ylabel('Standard Deviation (annualized) / sqrt(n)')
plt.title('Volatility Scaling of Returns From n-day Observations (Sim)')
plt.grid(True)
plt.show()

