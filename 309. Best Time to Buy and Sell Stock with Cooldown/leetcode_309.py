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
                profit = -prices[i] + dfs(i+1, not buy)
                cooldown = dfs(i+1, buy)
                cache[(i, buy)] = max(profit, cooldown)
            else:
                profit = prices[i] + dfs(i+2, not buy)
                cooldown = dfs(i+1, buy)
                cache[(i, buy)] = max(profit, cooldown)
            
            return cache[(i, buy)]
            
        return dfs(0, True)