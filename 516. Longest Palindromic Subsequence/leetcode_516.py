class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        n = len(s) - 1
        cache = {}
        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if (x, y) in cache:
                return cache[(x, y)]

            if s[x] == s2[y]:
                ans = 1 + dfs(x-1, y-1)
            else:
                ans1 = dfs(x-1, y)
                ans2 = dfs(x, y-1)
                ans = max(ans1, ans2)
            cache[(x, y)] = ans
            return cache[(x, y)]
        
        return dfs(n, n)
