class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hm = {i:[] for i in range(n)}
        for src, des in edges:
            hm[src].append(des)
            hm[des].append(src)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for nei in hm[node]:
                dfs(nei)

            return

        count = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1
        
        return count
        