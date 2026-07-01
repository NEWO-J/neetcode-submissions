class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy
        l = 0
        # sell
        r = 0
        result = [prices[0],prices[0]]
        profits = []
        bestprofit = 0
        while r < len(prices) - 1:
            if prices[r] >= prices[l]:
                r += 1
                if prices[r] > result[1]:
                    result[1] = prices[r]
            else: # prices[r] < prices[l] and prices[r] < lowest:
                l = r
                if prices[l] < result[0]:
                    result[0] = prices[l]
                    # We need to remove elements that appear chronologically earlier now
                    # If we reset we run the risk of neglecting the earlier superior buy/sell ratio.
                    # So we need to save it in a set
                    result[1] = prices[l]
                    
            profit = result[1] - result[0]
            if profit > bestprofit:
                bestprofit = profit


        return bestprofit