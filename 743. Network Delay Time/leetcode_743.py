class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i+1:[] for i in range(n)}
        for src, des, delay in times:
            adj[src].append((des, delay))

        ans = [-1] * (n)
        hq = [(0, k)]
        seen = set()

        while hq:
            delay, node = heapq.heappop(hq)
            if node in seen:
                continue
            
            seen.add(node)
            ans[node-1] = delay

            for nei, time in adj[node]:
                if nei not in seen:
                    heapq.heappush(hq, (delay+time, nei))
        
        if -1 in ans:
            return -1
        return max(ans)
        