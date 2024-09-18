class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        i = 0
        n = len(stones)
        while n > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()

            remainder = abs(stone1 - stone2)
            if remainder:
                stones.append(remainder)
                stones.sort()

            n = len(stones)
        return stones[0] if stones else 0