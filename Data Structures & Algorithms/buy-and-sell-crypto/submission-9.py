class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            i = 0
            j = 0

            buy_price = float('inf')
            sell_price = 0
            max_profit = 0

            while j < len(prices) - 1:
                if prices[j] < buy_price:
                    i = j
                    buy_price = prices[j]
                    sell_price = 0
                    j += 1
                else:
                    j += 1


                sell_price = max(sell_price, prices[j])

                max_profit = max(max_profit, (sell_price - buy_price))

                
            if sell_price - buy_price <= 0:
                return 0
            
            else: return max_profit
