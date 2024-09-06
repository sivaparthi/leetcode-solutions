class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        for i in range(len(nums1)):
            heapq.heappush(hq, (nums1[i]+nums2[0], i, 0))
        
        res = []
        while hq and len(res) < k:
            total, i, j = heapq.heappop(hq)
            res.append((nums1[i], nums2[j]))

            if j + 1 < len(nums2):
                heapq.heappush(hq,(nums1[i]+nums2[j+1], i, j+1))
        
        return res