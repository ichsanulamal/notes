## 1. Trend-Following Strategy with Reinforcement Learning API

### Lecture Overview

In this lecture, we’ll reimplement the trend-following strategy using the reinforcement learning (RL) paradigm. Our goal is to eventually achieve secure learning, but we'll take it step by step. This initial step will introduce key RL components: environment, states, actions, and rewards. 

### Motivation

Previously, when implementing trend-following, we had to shift returns—a process that likely felt unnatural. RL, however, operates over discrete time steps, allowing us to approach the problem more naturally. We'll eliminate the need for shifting data, making the process feel more like controlling a robot in a trading environment rather than manipulating a data frame.

### Step-by-Step Walkthrough

Let's start by considering a data frame with SPY closing prices, along with fast and slow moving averages (MAs) and daily log returns. Assume the returns are not shifted, meaning the return on each row corresponds to that day.

#### Example Scenario

Suppose we're at time \( t \) and we’re not currently invested. Today, the fast MA crosses above the slow MA, indicating a buy signal. We buy at today’s closing price, but the return we get is for tomorrow (time \( t+1 \)). This action brings us to the next day, and the reward for this action is the return at time \( t+1 \). This is an example of a Markov Decision Process (MDP) transition: we move from state \( S_t \) to \( S_{t+1} \) and receive a reward \( R_{t+1} \).

### Actions, States, and Rewards

- **States**: A vector containing the fast and slow MAs.
- **Rewards**: The daily log return.
- **Actions**: Buy, sell, or do nothing.

Previously, we used a column "is_invested" to track our position (invested or not), but this is more of a state than an action. The real actions are buying, selling, or holding.

#### Decision Logic

- **Do Nothing**: If we’re already invested and the fast MA is greater than the slow MA, or if we’re not invested and the fast MA is less than the slow MA.
- **Sell**: If we’re invested and the fast MA is less than the slow MA.

The strategy relies on whether the fast MA crosses the slow MA from above or below. This crossover is the key event, and the time in between is either a continuation of the trend or a reversal.

### Implementation Overview

We'll implement two central objects: the **Agent** and the **Environment**.

#### Environment

Inspired by the OpenAI Gym, the environment will manage the data and handle transitions. It will have two main functions:

1. **reset()**: Initializes the environment and returns the initial state.
2. **step(action)**: Executes an action, returns the next state, the reward, and a flag indicating if the episode is done.

#### Agent

The agent’s role is to decide which action to take based on the current state. It will have a single function:

- **act(state)**: Takes the current state as input and returns an action (buy, sell, or do nothing).

### Interaction between Agent and Environment

The interaction follows a simple loop:

1. Initialize the environment with `env.reset()`.
2. Set a flag `done` to `false` and initialize `total_reward` to `0`.
3. Loop until `done` is `true`:
   - Call `agent.act(state)` to decide the action.
   - Execute the action with `env.step(action)`, receiving the next state, reward, and `done` flag.
   - Update the `total_reward`.
   - Optionally, call `agent.train()` to update the agent’s logic (not needed for trend-following).
   - Update `state` to the new state.

### Pseudocode Summary

- **Environment**:
  - `reset()` sets `current_index` to 0 and initializes the state.
  - `step(action)` increments `current_index`, updates `is_invested` based on the action, computes the reward, and returns the next state, reward, and done flag.

- **Agent**:
  - `act(state)` decides to buy, sell, or do nothing based on the state and whether we’re currently invested.

### Conclusion

This setup provides a clear structure for a reinforcement learning program. You’ve learned how the agent and environment interact and the logic that drives their behavior. In more advanced RL tasks, the environment might exist outside your program, such as in OpenAI Gym or real-world scenarios like robotics.

## 2. Trend-Following Strategy Revisited

In this lecture, we will reimplement the trend-following strategy using a reinforcement learning (RL) framework. This time, we'll work with explicit environment and agent objects that interact with each other. You can refer to the title of the notebook to see which specific notebook we are using. Although much of the initial setup will be similar to what we've done before, I'll review everything in case you need a refresher on reinforcement learning.

### Step 1: Downloading Data
We'll start by downloading the SPY CSFI dataset. Since we are focusing on trend following, we only need the daily closing prices.

### Step 2: Importing Libraries
Next, we'll import the necessary libraries: `pandas`, `numpy`, and `matplotlib`.

### Step 3: Preparing the Data
We'll load and preprocess the CSFI data, calculating the fast and slow moving averages (SMAs). We'll create a variable, `FTS`, to store the column names of these moving averages. We will also calculate the log returns by taking the logarithm of the close prices and then computing the differences.

### Step 4: Splitting Data
We'll split our dataset into training and testing sets, reserving the last 1,000 data points for testing.

### Step 5: Implementing the Environment Class
Now, we’ll create the `Environment` class. 

- **Constructor:** The constructor takes a single argument, which is a DataFrame (either the train or test data). Inside, we store this DataFrame in an instance variable, `df`, and set `N` to the length of `df`, which helps us determine when we reach the end of the data. We also initialize `current_index` to 0, which tracks our position in the DataFrame. The action space is defined as integers `0`, `1`, and `2`, representing buy, sell, and hold actions, respectively. We set an `invested` flag to `0` or `1` to indicate whether we are holding a position. The `states` instance variable will hold the columns specified by the feature list, converted to a NumPy array for convenient indexing. We also store the log returns and initialize the `total_buy_and_hold` variable to accumulate returns throughout the episode.

- **Reset Function:** This function resets `current_index` to 0, `total_buy_and_hold` to 0, and the `invested` flag to 0. It returns the initial state, which corresponds to the data at `index 0`.

- **Step Function:** The `step` function takes one argument, `action`, and returns the next state, reward, and a `done` flag. We increment `current_index`, check if it exceeds `N` (raising an exception if it does), and then update the `invested` flag based on the action. The reward is computed based on whether the agent is invested. We then retrieve the next state and update the `total_buy_and_hold` counter. The `done` flag is set to `True` if `current_index` is equal to `N-1`. Finally, we return the next state, reward, and `done` flag.

### Step 6: Implementing the Agent Class
Next, we define the `Agent` class.

- **Constructor:** The constructor initializes an `is_invested` flag to `False`.

- **Act Function:** The `act` function takes in the `state` and determines the appropriate action. If the fast SMA is greater than the slow SMA and the agent is not invested, the agent buys. If the fast SMA is less than the slow SMA and the agent is invested, the agent sells. Otherwise, the agent holds. We return `0` for buy, `1` for sell, and `2` for hold.

- **Play Episode Function:** This function runs an episode, taking in an `agent` and an `env` (environment) as arguments. We start by resetting the environment and initializing the `done` flag to `False` and `total_reward` to 0. Inside a loop, which continues until `done` is `True`, the agent takes an action based on the current state, and the environment returns the next state, reward, and `done` flag. We accumulate the reward and update the state. Finally, we return the total reward.

### Step 7: Running the Strategy
Finally, we’ll put everything together:

- We create two environments: one for training and one for testing.
- We instantiate the agent.
- We call `play_one_episode` with the agent on the training environment, and then on the testing environment.
- We print out the training reward and the buy-and-hold total for the training set, which should be around `0.43` and `0.597`, matching previous results.
- We also print out the test reward and buy-and-hold total for the test set, which should be around `0.08889` and `0.193`, again matching previous outcomes.

### Conclusion
This lecture aimed to solidify your understanding of a few key concepts. First, it should have clarified our earlier code by demonstrating a more realistic implementation of an agent and environment. Second, you learned about important reinforcement learning components, including the environment, agent, states, actions, and rewards. With this foundation, transitioning to learning scripts will feel like a natural extension of what we’ve covered so far.

## 3. Q-Learning in an Algorithmic Trading Context

**Lecture Overview:**

In this lecture, we'll dive into the basics of Q-learning within a financial engineering context. Think of this session as a quick guide to reinforce your learning. If spending hours on pure reinforcement learning theory isn't appealing to you, this lecture can offer a fresh perspective. However, it's still recommended to delve into the theory for a deeper understanding.

**Key Concept: The Q-Table**

Unlike our previous discussions on trend-following algorithms, in this lecture, our agent will actively learn and use its experience to improve future outcomes. The core concept we’ll introduce is the Q-Table. Imagine a table where the rows represent states and the columns represent actions. Each entry in this table, Q(s, a), represents the expected return (sum of future rewards) for taking action 'a' in state 's'. 

This Q-Table is a crucial tool for our agent to decide which action to take at any given state. The goal is to find the action that maximizes future rewards by selecting the action with the highest Q-value.

**Understanding States and Actions:**

Actions are straightforward—they can be represented as integers like 0, 1, or 2, corresponding to different columns in the table. States, however, are more complex and aren’t naturally represented as integers. We'll cover how to encode states in the next lecture, but for now, we'll assume that we can organize them in a table format.

**The Meaning of Q-Values:**

The Q-value, Q(s, a), represents the expected sum of future rewards when taking action 'a' in state 's'. This "return" should not be confused with financial returns; here, it refers to the total rewards accumulated over time. 

Given this definition, choosing the best action becomes simple: select the action that maximizes Q(s, a). While this might seem circular, if the Q-table is accurate, it will guide the agent to make optimal decisions by comparing the Q-values across all possible actions.

**Updating the Q-Table:**

To ensure the Q-table contains accurate values, we use a process called Q-learning. Q-learning is essentially a method of updating the Q-table using an exponentially weighted moving average. This method reflects how learning from experience works.

The idea is to update Q(s, a) based on the reward received after taking action 'a' in state 's', plus the expected future rewards (estimated by the maximum Q-value in the next state). This update process is similar to calculating a sample mean, where we adjust our estimate with new information over time. Mathematically, this update process is akin to gradient descent, a concept familiar to those with a background in machine learning.

**Implementing Q-Learning:**

Our agent needs two key functions: `act` and `train`. 

- **Act Function:** The `act` function determines which action to take. Instead of always choosing the best-known action, the agent occasionally selects a random action to explore new possibilities. This balance between exploiting known information and exploring new options is managed by a parameter called epsilon (ε).

- **Train Function:** The `train` function updates the Q-table based on the agent's experiences. It takes as input the state, action, reward, next state, and a flag indicating if the next state is terminal. If the next state is terminal, the Q-value update is simple: the expected future reward is zero. Otherwise, the Q-value is updated based on the reward received and the maximum expected future reward from the next state.

**Conclusion:**

This lecture provided a concise introduction to Q-learning, integrating concepts we've previously covered. We've learned how to use the Q-table to guide our agent's actions and how to update the table to improve decision-making over time. These concepts are central to the `act` and `train` functions of our agent class, laying the foundation for more advanced learning techniques.

## 4. Representing States

### Lecture Overview

In this lecture, we'll focus on a key topic that was intentionally left out of the previous lecture: **How do we represent states?** 

### Recap and Introduction

Before diving in, let's clarify the type of data we'll use. Remember, one of the main themes of this course is that your data can be anything. It's up to you to select something useful. For simplicity and comparison, we'll stick with the same data used in our machine learning scripts: **the previous day's returns for various stocks in the S&P 500.**

### The Challenge: Continuous vs. Discrete States

However, there's a challenge. Returns are continuous variables, meaning there are infinitely many possible values. For our approach to be manageable, we need to convert these continuous values into discrete states. But how do we do this?

### Solution: Binning

One simple solution is **binning**. Here's how it works:

1. **Define Bins:** Suppose we have three bins:
   - Bin 1: Values from \(-\infty\) to 0
   - Bin 2: Values from 0 to 1
   - Bin 3: Values from 1 to \(+\infty\)

2. **Assign Values to Bins:** This process transforms an infinite number of possible returns into a finite number of bins.

#### Defining Useful Bins

The next step is to define your bins effectively. The scheme mentioned above is overly simplistic since most returns are close to zero. Instead, consider the following:

- **Maximum and Minimum Values:** Split the range between these two into, say, 10 equal parts. 
- **Return Distributions:** Keep in mind that returns follow a distribution, with some values being more likely (usually near zero) and others less likely. You don’t want a single bin handling rare extreme returns, nor do you want 90% of your returns in one bin.

**Goal:** Define bins according to frequency. High-frequency areas should have smaller bins, and low-frequency areas should have larger bins, with the outermost bins extending to infinity.

### Implementation: Using NumPy’s `digitize`

Now, let's talk about implementation.

#### Binning with NumPy

If we know the bin boundaries and have a value, we can determine which bin it belongs to using NumPy's `digitize` function. Here’s an example:

- **Bins:** Defined as `[0, 1, 2.5, 4, 10]`
- **Values (`X`):** `[0.2, 6.4, 2.9, 1.1]`
- **Bin Assignments:** `[1, 4, 3, 2]`

**Explanation:**
- `0.2` falls between 0 and 1, so it goes into bin 1.
- `6.4` falls between 4 and 10, so it goes into bin 4.

#### Handling Out-of-Bounds Values

What happens if a value falls outside the defined bin boundaries? For example:
- **Value `-1`:** Below the smallest boundary, assigned to bin 0.
- **Value `11`:** Above the largest boundary, assigned to bin 5.

This makes sense because the complete set of bins includes 0, 1, 2, 3, 4, and 5.

### Finding Bin Boundaries

Next, let's discuss how to determine the boundaries:

1. **Sort the Returns:** Start by sorting the returns from smallest to largest.
2. **Determine Equal Spacing:** If you have 100 elements and want 10 bins, identify equally spaced elements within the sorted array.

**Important Detail:** The boundaries should be centered to handle values extending to infinity, not just aligned with the smallest and largest values. For instance, boundaries could be 5, 15, 25, etc., up to 95, ensuring that extreme values also fit within these bins.

### Representing the Q-Table

Since we’re dealing with returns from multiple stocks, our state will be a tuple of integers rather than a single integer. Python’s dictionary is perfect for this, as it allows immutable objects like tuples to be used as keys.

- **State Representation:** Tuple of multiple integers.
- **Action Representation:** A single integer.

Thus, our "table" will be an array indexed by these objects, essentially functioning as a dictionary.

### Conclusion and Advice

This was a brief overview of how we'll represent states in the upcoming code. It's a complex topic, so don’t worry if it doesn't all make sense right away. I encourage you to revisit this lecture as needed, and feel free to develop your own solutions if my approach doesn't resonate with you. My goal is to teach the concepts and provide an example implementation. It's not necessarily the fastest or most "Pythonic" way, but it's designed to be clear and understandable.

Always aim to implement things in a way that makes the most sense to you.

## 5. Q-Learning for Algorithmic Trading

In this lecture, we'll finally implement our learning trader. The script will use the same data as our machine learning script, so we'll need to download the full S&P dataset.

#### Setup

First, we'll import the necessary libraries: Pandas, NumPy, Matplotlib, and some additional tools. You'll see how these tools are used shortly. Next, we'll load our DataFrame using `pd.read_csv`. Since you've already seen how we process this data, we'll go through it quickly:

1. **Drop Rows with Missing Values**: We start by dropping any rows that have all missing values, as these rows are irrelevant.
2. **Drop Columns with Missing Values**: Next, we drop any columns with at least one missing value, to avoid the need for forward or backfilling.
3. **Generate Log Returns**: We create a new DataFrame containing the log returns for each S&P component.
4. **Split Data**: We split the data into training and testing sets using the returns DataFrame.
5. **Select Input Features**: We specify that our input features will be Apple, Microsoft, and Amazon.

It's important to note that because we're using binning, the state space will grow exponentially. For instance, if each column has 10 bins and we have three columns, the total number of unique bins is \(10 \times 10 \times 10 = 1000\). With more features, the state space grows exponentially, leading to increased time and space requirements.

#### The `Environment` Class

This class is mostly the same as before, so we'll go through it quickly. The main difference is that now, the rewards are derived from the SPY column of the DataFrame. The features are also different but are specified by a variable called `fts`.

#### The `StateMapper` Class

This is likely the most complex part of the script and relies heavily on the theory covered earlier. If you're not quite getting it, I recommend revisiting the theory lecture.

- **Purpose**: The `StateMapper` object transforms a continuous vector of states into the correct bins.
- **Constructor**: The constructor defines the bin boundaries. It takes an object and a `bins` parameter, which specifies the number of bin boundaries and the number of samples. 

  - **Step 1**: Create an empty list called `states` to store the states we collect.
  - **Step 2**: Set `done` to `False` and initialize the environment.
  - **Step 3**: Set an instance variable `D` to the length of the state vector, which is the number of sets of bins we need to create.
  - **Step 4**: Append the initial state to our list of states.
  - **Step 5**: Enter a loop that iterates `n_samples` times. Inside the loop:
    - Choose a random action from the environment's action space.
    - Call `env.step()` with the random action, which gives us the next state. Append this state to our list.
    - Check if we're done; if so, reset the environment and start again.
  - **Step 6**: After collecting the states, cast them to a NumPy array for easy indexing.
  - **Step 7**: Create the bin boundaries for each column of data. Start by initializing an empty list `self.bins`.
  - **Step 8**: Loop through each dimension:
    - For each column, initialize an empty list `current_bin` to store the boundaries.
    - Loop `bins` times to calculate the boundaries using the formula: 
      \[
      \text{Boundary} = \frac{n\_samples}{n\_bins} \times (k + 0.5)
      \]
      This ensures centered bin boundaries. Plugging in example numbers can help clarify the logic.

- **Transform Function**: This function converts a continuous state vector into the corresponding bin tuple:
  - **Step 1**: Create an array of zeros called `x`, where we'll store the bin values.
  - **Step 2**: Loop through each dimension, using `np.digitize` to determine the bin for each state value.
  - **Step 3**: Cast `x` to a tuple and return it.

- **All Possible States Function**: This function is essential for initializing the Q-table. Since Q-values are updated iteratively, each state-action pair must have an initial value. The function uses `itertools.product` to generate all possible combinations of bins for each dimension.

#### The `Agent` Class

This class is more complex than our trend-following agent, as it incorporates learning.

- **Constructor**: Takes in the `action_size` and a `StateMapper` object.
  - **Instance Variables**: These include `action_size`, `gamma`, `epsilon`, `learning_rate`, and `state_mapper`.
  - **Q-table Initialization**: We initialize `Q` as an empty dictionary and loop through all possible states and actions, assigning each state-action pair a random initial value drawn from the standard normal distribution.

- **Action Selection Function**: This function implements an epsilon-greedy strategy:
  - Generate a random number. If it's less than `epsilon`, return a random action.
  - Otherwise, transform the state into its bin representation, look up the Q-values for all possible actions, and return the action with the highest Q-value.

- **Train Function**: Implements the Q-learning formula:
  - Transform the current and next states into their bin representations.
  - If the next state is terminal, the target is equal to the reward. Otherwise, calculate the target as the reward plus the discounted maximum Q-value for the next state.
  - Update the Q-value for the current state-action pair using the learning formula.

- **Play One Episode Function**: Similar to the earlier implementation, but with an additional `is_train` argument. If `is_train` is `True`, the agent will learn during this episode.

#### Running the Model

Finally, we put everything together:

1. Set the number of episodes to 500.
2. Create two environments: one for training and one for testing.
3. Set the action size, instantiate the `StateMapper` and `Agent`.
4. Create empty arrays to store the total rewards for each episode in both training and testing.
5. Loop through the episodes:
   - Train the agent on the training environment.
   - Test the agent on the test environment, setting `epsilon` to 0 to prevent exploration during testing.
6. Print the episode number and the rewards for both training and test.

#### Plotting the Results

Finally, plot the rewards for both training and test sets. You'll observe that while the model performs better on the training set (as expected), it generally outperforms a buy-and-hold strategy on the test set as well. Also, as the agent learns, the variability in test rewards decreases, indicating more consistent and intelligent performance rather than random luck.

