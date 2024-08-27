class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        hm = {i:[] for i in range(n)}
        for a, b in redEdges:
            hm[a].append([b, "red"])
        for u, v in blueEdges:
            hm[u].append([v, "blue"])

        def bfs(target):
            seen = set()
            q = deque()
            q.append([0,0, None, None])
            seen.add((0, None))

            while q:
                node, moves, prev_color, curr_color = q.popleft()
                if node == target and prev_color == None and curr_color == None:
                    return moves
    
                if (node == target and prev_color != curr_color) or (node == target and prev_color == None):
                    return moves

                for n, color in hm[node]:
                    if color != curr_color and (n, color) not in seen:
                        q.append([n, moves+1, curr_color, color])
                        seen.add((n, color))
            return -1
        
        res = []
        for i in range(n):
            ans = bfs(i)
            res.append(ans)
        return res


# not the best looking or optimised code. But Will rework on this problem.