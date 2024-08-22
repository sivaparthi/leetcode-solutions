class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        hm = {i:[] for i in range(len(quiet))}

        for a, b in richer:
            hm[b].append(a)
        res = []
        cache = {}
        def dfs(person, seen):
            if person in cache:
                return cache[person]
            quietest = person
            for p in hm[person]:
                candidate = dfs(p, seen)
                if quiet[candidate] < quiet[quietest]:
                    quietest = candidate
            cache[person] = quietest
            return quietest
        
        for i in range(len(quiet)):
            ans = dfs(i, [])
            res.append(ans)
        return res

# graphs --> topological sort
# Time complexity -> O(n)