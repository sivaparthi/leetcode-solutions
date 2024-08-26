class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hm = {i:[] for i in range(numCourses)}
        for p, c in prerequisites:
            hm[c].append(p)

        def dfs(course, preq):
            if course in seen:
                return
            
            if course == preq:
                return True

            seen.add(course)
            for c in hm[course]:
                if dfs(c, preq):
                    return True
            
            return False
        
        answer = []
        for p, c in queries:
            seen = set()
            ans = dfs(c, p)
            answer.append(ans)
        
        return answer