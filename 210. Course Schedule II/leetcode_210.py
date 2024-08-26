class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            hm[c].append(p)
        
        res = []
        seen = set()
        visited = set()

        def dfs(course):
            
            if course in visited:
                return True
            if course in seen:
                return False
            if hm[course] == []:
                res.append(course)
                visited.add(course)
                return True
            seen.add(course)
            for c in hm[course]:
                if not dfs(c):
                    return False
            
            res.append(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


# Topological sort