# Task 2: Price a commodity storage contract

Here is the background information on your task

Great work! The desk now has the price data they need. The final ingredient before they can begin trading with the client is the pricing model. Alex tells you the client wants to start trading as soon as possible. They believe the winter will be colder than expected, so they want to buy gas now to store and sell in winter in order to take advantage of the resulting increase in gas prices. They ask you to write a script that they can use to price the contract. Once the desk are happy, you will work with engineering, risk, and model validation to incorporate this model into production code.

The concept is simple: any trade agreement is as valuable as the price you can sell minus the price at which you are able to buy. Any cost incurred as part of executing this agreement is also deducted from the overall value. So, for example, if I can purchase a million MMBtu of natural gas in summer at $2/MMBtu, store this for four months, and ensure that I can sell the same quantity at $3/MMBtu without incurring any additional costs, the value of this contract would be ($3-$2) *1e6 = $1million. If there are costs involved, such as having to pay the storage facility owner a fixed fee of $100K a month, then the 'value' of the contract, from my perspective, would drop by the overall rental amount to $600K. Another cost could be the injection/withdrawal cost, like having to pay the storage facility owner $10K per 1 million MMBtu for injection/withdrawal, then the price will further go down by $10K to $590K. Additionally, if I am supposed to foot a bill of $50K each time for transporting the gas to and from the facility, the cost of this contract would fall by another $100K. Think of the valuation as a fair estimate at which both the trading desk and the client would be happy to enter into the contract. 

# Prototype Pricing Model for Gas Contracts

## Overview

You need to create a prototype pricing model that can go through further validation and testing before being put into production. The goal is to eventually have a model that can serve as the basis for fully automated quoting to clients. However, for the current stage, the desk will use it with manual oversight to explore options with the client.

## Function Requirements

Write a function that utilizes the previously created data to price the contract. The model should be able to handle multiple dates for injecting and withdrawing a set amount of gas. Consider all the cash flows involved in the product.

### Input Parameters

The input parameters that should be taken into account for pricing are:

- Injection dates.
- Withdrawal dates.
- Prices at which the commodity can be purchased/sold on those dates.
- The rate at which the gas can be injected/withdrawn.
- The maximum volume that can be stored.
- Storage costs.

### Assumptions

- There is no transport delay.
- Interest rates are zero.
- Market holidays, weekends, and bank holidays need not be accounted for.

## Pricing Function

Write a function that takes the aforementioned inputs and returns the value of the contract.

```python
def price_gas_contract(injection_dates, withdrawal_dates, purchase_prices, sale_prices, injection_rate, withdrawal_rate, max_volume, storage_costs):
    # Your pricing logic here
    pass
