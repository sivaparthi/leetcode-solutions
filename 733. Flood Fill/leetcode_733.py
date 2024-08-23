class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        seen = set()

        def dfs(x, y, source):
            if x < 0 or y < 0 or x >= row or y >= col or (x, y) in seen or image[x][y] != source:
                return
            
            seen.add((x, y))
            image[x][y] = color
            dfs(x+1, y, source)
            dfs(x-1, y, source)
            dfs(x, y+1, source)
            dfs(x, y-1, source)
            return

        dfs(sr, sc, image[sr][sc])

        return image