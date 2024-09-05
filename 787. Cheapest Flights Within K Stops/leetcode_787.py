class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for from_city, to_city, cost in flights:
            adj[from_city].append((to_city, cost))


        hq = [(0, src, 0)] # cost, city, stops
        visited = {}

        while hq:
            cost, city, stops = heapq.heappop(hq)
            
            if city == dst:
                return cost

            if stops > k:
                continue
            
            if city not in visited or stops < visited[city]:
                visited[city] = stops
                for next_city, next_cost in adj[city]:
                    heapq.heappush(hq, (cost + next_cost, next_city, stops + 1))

        return -1