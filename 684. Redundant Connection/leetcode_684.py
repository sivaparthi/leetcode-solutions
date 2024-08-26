class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vals = []
        for i, j in edges:
            vals.append(i)
            vals.append(j)
        n = max(vals)
        size = [1] * (n+1)
        parent = [i for i in range(n+1)]

        def find_ultimate_parent(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = find_ultimate_parent(parent[node])
            return parent[node]

        def union(u, v):
            p1 = find_ultimate_parent(u)
            p2 = find_ultimate_parent(v)
            s1 = size[p1]
            s2 = size[p2]
            if p1 == p2:
                return 0
            if s1 < s2:
                parent[p1] = p2
                size[p2] += size[p1]
            else:
                parent[p2] = p1
                size[p1] += size[p2]
            return 1

        components = n
        res = []
        for u, v in edges:
            ans = union(u, v)
            components -= ans
            if ans == 0:
                res.append([u, v])
        return res[-1]
    
# Disjoint set