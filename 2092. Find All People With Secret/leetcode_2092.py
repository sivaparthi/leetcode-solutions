class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj_list = defaultdict(list)
        for from_person, to_person, time in meetings:
            adj_list[from_person].append((to_person, time))
            adj_list[to_person].append((from_person, time))
        
        adj_list[0].append((firstPerson, 0))

        hq = [(-1, 0)]
        seen = set()

        while hq:
            time, person = heapq.heappop(hq)
            if person in seen:
                continue
            
            seen.add(person)

            for next_person, t in adj_list[person]:
                if t >= time:
                    heapq.heappush(hq, (t, next_person))

        res = list(seen) 
        return res