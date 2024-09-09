class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        bottom = n
        left = 0
        right = n

        res = [[-1 for i in range(n)] for j in range(n)]
        print(res)
        num = 1
        
        while top < bottom and left < right and num < (n*n)+1:
            for i in range(left, right):
                res[left][i] = num
                num += 1
            top += 1

            for i in range(top, bottom):
                res[i][right-1] = num
                num += 1
            right -= 1

            if not (top < bottom and left < right and num < (n*n)+1):
                break
            
            for i in range(right-1, left-1, -1):
                res[bottom-1][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1
        
        return res