from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
    
    def maxProfit_1(self, prices: List[int]) -> int:
        l,r =0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
               profit = prices[r] - prices[l]
               maxP = max(maxP, profit) 
            else:
               l = r
            r += 1 

        return maxP

if __name__=='__main__':
    print(":    :")
    nums = [1,2,3,4] 

    s1 = Solution()
    print(s1.maxProfit(nums))      
    print(s1.maxProfit_1(nums))  