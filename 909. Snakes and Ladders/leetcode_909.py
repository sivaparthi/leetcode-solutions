class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        adjusted_board = board[::-1]
        for i in range(1, len(adjusted_board), 2):
            adjusted_board[i] = adjusted_board[i][::-1]

        n = len(board)
        def get_cords(square):
            c = (square-1) % n
            r = math.floor((square-1)/n)
            return [r, c]
        
        q = deque()
        q.append([1, 0]) # --> square, no of moves made to reach there
        seen = set()
        ans = 0
        while q:
            square, moves = q.popleft()
            moves += 1
            for i in range(1,7):
                nextSquare = square + i
                r, c = get_cords(nextSquare)
                if adjusted_board[r][c] != -1:
                    nextSquare = adjusted_board[r][c]
                if nextSquare == n * n:
                    return moves
                if nextSquare not in seen:
                    seen.add(nextSquare)
                    q.append([nextSquare, moves])

        return -1