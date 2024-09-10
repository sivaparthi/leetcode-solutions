# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        if head:
            first = head
        else:
            return None
        if head.next:
            second = head.next
        else:
            return head

        while second != None:
            gcd = get_gcd(first.val, second.val)
            new_node = ListNode(gcd, None)
            new_node.next = first.next
            first.next = new_node
            first = second
            second = second.next
        
        return head