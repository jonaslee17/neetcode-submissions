class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                difference = prices[r] - prices[l]
                maxProfit = max(maxProfit, difference)
                r +=1
            else:
                l = r
                r+=1
        
        return maxProfit
            