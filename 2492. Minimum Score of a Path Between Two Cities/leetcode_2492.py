class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        hm = {i + 1: [] for i in range(n)}
        for u, v, d in roads:
            hm[u].append([v, d])
            hm[v].append([u, d])
        
        seen = set()
        min_distance = float("inf")
        
        def dfs(city):
            nonlocal min_distance
            if city in seen:
                return
            seen.add(city)
            for neighbor, distance in hm[city]:
                min_distance = min(min_distance, distance)
                dfs(neighbor)

        dfs(1)
        return min_distance
