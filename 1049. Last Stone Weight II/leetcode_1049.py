from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        n = len(stones)

        def dfs(i, total):
            if i >= n:
                return abs(total)
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            # Explore both options: add or subtract the current stone
            add = dfs(i+1, total + stones[i])
            subtract = dfs(i+1, total - stones[i])
            
            memo[(i, total)] = min(add, subtract)
            return memo[(i, total)]
        
        return dfs(0, 0)