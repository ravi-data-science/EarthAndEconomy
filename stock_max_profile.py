
#!/bin/python3

#from types import List
#from ast import List
from typing import List
import math
import os
import random
import re
import sys


def is_max_profit(prices: List[int]) -> int: 
    l,r = 0,1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            print(maxP)
            print(profit)
            #maxP = max(maxP - profit)
        else:
            l = r
        r += 1
    return maxP        


def maxProfit(prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


if __name__ == '__main__':

    stock_prices = [7,3,5,6,7]
    #maxP = is_max_profit(stock_prices)

    print(maxProfit(stock_prices))
    