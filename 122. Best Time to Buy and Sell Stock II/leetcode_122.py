class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        def dfs(i, buy):
            if i >= n:
                return 0
            if (i, buy) in cache:
                return cache[(i, buy)]
            if buy:
                profit = -prices[i] + dfs(i+1, False)
                ignore_profit = dfs(i+1, buy)
                max_profit = max(profit, ignore_profit)
                cache[(i, buy)] = max_profit
            else:
                profit = prices[i] + dfs(i+1, True)
                ignore_profit = dfs(i+1, buy)
                max_profit = max(profit, ignore_profit)
                cache[(i, buy)] = max_profit
            return cache[(i, buy)]
        
        return dfs(0, True)
            