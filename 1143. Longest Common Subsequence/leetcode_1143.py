# Memoization Solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        cache = {}
        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if (x, y) in cache:
                return cache[(x, y)]
            ans = 0
            if text1[x] == text2[y]:
                ans = 1 + dfs(x-1, y-1)
            
            else:
                ans = 0 + max(dfs(x-1, y), dfs(x, y-1))
            
            cache[(x, y)] = ans
            return cache[(x, y)]
        
        res = dfs(m-1, n-1)
        return res


