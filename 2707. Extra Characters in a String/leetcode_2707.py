class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dictionary_set = set(dictionary)
        cache = {}

        def dfs(i):
            if i >= len(s):
                return 0
            
            if i in cache:
                return cache[i]

            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary_set:
                    res = min(res, dfs(j + 1))
            
            cache[i] = res
            return cache[i]
        
        return dfs(0)