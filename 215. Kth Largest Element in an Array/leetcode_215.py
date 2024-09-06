class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for i in range(len(nums)):
            heapq.heappush(hq, (-1 * nums[i]))

        for i in range(k):
            popped = heapq.heappop(hq)
        return popped * -1