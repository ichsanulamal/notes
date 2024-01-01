## Background Information

As a quantitative researcher within a commodity trading desk, you've been tasked with addressing a request from Alex, a Vice President (VP) on the desk. Alex intends to initiate trading in natural gas storage contracts. However, the current available market data needs enhancement to ensure accurate pricing of this financial instrument. Alex has contacted you via email seeking assistance in extrapolating the existing data obtained from external feeds. The goal is to provide more detailed granularity while considering the seasonal trends in pricing concerning different months of the year. The objective is to gather historical data and formulate an estimation model for the future price of gas at any given date.

## Commodity Storage Contracts Overview

Commodity storage contracts typically involve agreements between warehouse (storage) owners and various participants in the commodity supply chain, including refineries, transporters, distributors, among others. These contracts entail storing a specified quantity of a physical commodity (such as oil, natural gas, or agricultural products) in a warehouse for a predetermined duration. The crucial terms of such contracts, such as periodic storage fees and limitations on withdrawals or injections of the commodity, are established at the inception of the agreement between the warehouse owner and the client.

The injection date marks when the commodity is purchased and stored, while the withdrawal date denotes when the stored commodity is withdrawn and sold.

## Participants in Commodity Storage Contracts

Clients involved in commodity storage contracts encompass various entities within the commodities supply chain. This includes but is not limited to producers, refiners, transporters, and distributors. Additionally, this group encompasses firms engaged in commodities trading, hedge funds, and other entities whose primary objective revolves around leveraging seasonal or intra-day price differentials in physical commodities.

For instance, a firm seeking to purchase physical natural gas during the summer months to sell it during winter aims to capitalize on the seasonal price differentials mentioned earlier. To execute this strategy effectively, the firm would require the services of an underground storage facility to stockpile the purchased inventory and realize profits.


# Task Description

Here is your task:

After asking around for the source of the existing data, you learn that the current process is to take a monthly snapshot of prices from a market data provider, which represents the market price of natural gas delivered at the end of each calendar month. This data is available for roughly the next 18 months and is combined with historical prices in a time series database. After gaining access, you are able to download the data in a CSV file.

- Download the monthly natural gas price data.
- Each point in the data set corresponds to the purchase price of natural gas at the end of a month, from 31st October 2020 to 30th September 2024.
- Analyze the data to estimate the purchase price of gas at any date in the past and extrapolate it for one year into the future. 
- Your code should take a date as input and return a price estimate.
- Try to visualize the data to find patterns and consider what factors might cause the price of natural gas to vary. This can include looking at months of the year for seasonal trends that affect the prices, but market holidays, weekends, and bank holidays need not be accounted for. Submit your completed code below.

**Note:** This role often requires the knowledge and utilization of data analysis and machine learning. Python is a useful tool and one that JPMorgan Chase uses a lot in quantitative research since it’s capable of completing complex tasks.

Moving forward in this program, the example answers are given in Python code. (If Python is not downloaded on your system, you can execute Python code in Jupyter Notebook online for free.)
