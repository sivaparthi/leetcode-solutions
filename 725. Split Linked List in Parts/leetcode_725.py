# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        parts_length = []
        q = count // k # quotient
        remainder = count % k

        for i in range(k):
            if i < remainder:
                parts_length.append(q+1)
            else:
                parts_length.append(q)

        res  = []
        for i in parts_length:
            temp = head
            first = head
            count = 1
            while temp and count < i:
                count += 1
                temp = temp.next
            if temp:
                head = temp.next
                temp.next = None
                res.append(first)
            else:
                res.append(None)
        return res