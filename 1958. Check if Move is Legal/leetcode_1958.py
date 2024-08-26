class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [[0, 1], [1, 0], [0,-1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        # length = 1
        def dfs(x, y, color, dire, length):
            r , c = dire
            currow, curcol = x+r, y+c
            
            while (currow < row and currow >= 0 and curcol < col and curcol >= 0):
                # print(currow, curcol)
                length += 1
                if board[currow][curcol] == '.':
                    return False
                if board[currow][curcol] == color:
                    if length >= 3:
                        return True
                    else:
                        return False

                currow, curcol = currow + r, curcol + c
            return False    

        for dire in directions:
            if dfs(rMove, cMove, color, dire, 1):
                return True
            
        return False