class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r= 0, 1
        maxProfit= 0
        while r < len(prices):
            if prices[r] > prices[l]:
                dif = prices[r] - prices[l]
                maxProfit = max(maxProfit, dif)
                r += 1
            else:
                l = r
                r += 1
        return maxProfit

            

            