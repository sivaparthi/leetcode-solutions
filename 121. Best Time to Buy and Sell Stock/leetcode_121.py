class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cache = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in cache:
                return cache[(i, buy)]
            
            if buy:
                buy_price = -prices[i] + dfs(i+1, False)
                ignore = dfs(i+1, buy)
                cache[(i, buy)] = max(buy_price, ignore)
            else:
                sell_price = prices[i]
                ignore = dfs(i+1, buy)
                cache[(i, buy)] = max(sell_price, ignore)
            
            return cache[(i, buy)]
        
        return dfs(0, True)