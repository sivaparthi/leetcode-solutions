from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1           # --> edge case 1
        if target == '0000':
            return 0            # --> edge case 2


        q = deque([("0000", 0)])  # state, moves
        seen = {"0000"}  # Set to track visited states

        while q:
            state, moves = q.popleft()

            for i in range(4):
                digit = int(state[i])
                
                # Move the digit up and down (circularly)
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    next_state = state[:i] + str(new_digit) + state[i + 1:]

                    if next_state == target:
                        return moves + 1
                    if next_state not in deadends and next_state not in seen:
                        seen.add(next_state)
                        q.append((next_state, moves + 1))

        return -1
