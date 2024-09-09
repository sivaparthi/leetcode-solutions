# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        linked_list = []

        temp = head

        while temp:
            linked_list.append(temp.val)
            temp = temp.next

        res = [[-1 for i in range(n)] for j in range(m)]
        left = 0
        right = n
        top = 0
        bottom = m

        end = len(linked_list)
        start = 0
        while left < right and top < bottom and start < end:
            if start < end:
                for i in range(left, right):
                    print(start)
                    res[top][i] = linked_list[start]
                    start += 1
                    if start == end:
                        break
                top += 1

            if start < end:
                for i in range(top, bottom):
                    res[i][right-1] = linked_list[start]
                    start += 1
                    if start == end:
                        break
                right -= 1

            if not (left < right and top < bottom and start < end):
                break
            
            if start < end:
                for i in range(right-1, left-1, -1):
                    res[bottom-1][i] = linked_list[start]
                    start += 1
                    if start == end:
                        break
                bottom -= 1

            if start < end:
                for i in range(bottom-1, top-1, -1):
                    res[i][left] = linked_list[start]
                    start += 1
                    if start == end:
                        break
                left += 1

        return res 