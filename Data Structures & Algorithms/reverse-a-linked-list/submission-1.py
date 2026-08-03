# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # so we need to set the next element as the previous
        # but once we try to set the previous element to the next
        # we 
        previous = None
        curr = head

        while curr:
            n = curr.next
            curr.next = previous
            previous = curr
            curr = n
           
        return previous


