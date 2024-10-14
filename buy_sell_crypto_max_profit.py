if __name__ == '__main__':
    prices = [2,5,4,7,8,4,9]
    l, r = 0,1
    maxProfit = 0

    while r < len(prices):
        if (prices[l] < prices[r]):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit,profit)
        else:
            l = r #move all the way to right pointer to lowest value
        r += 1

    print(maxProfit)        
