# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        merged = ListNode()
        tail = merged
        
        while curr1 and curr2:
            # look at the current of list 1, is it bigger or smaller than that of the second list

            # if larger then we need curr2 to be inserted into the list and then skip to curr2.next then redo the same operation
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
                
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next
        
        # once any list runs out of element, we find the one that does
        # and point the tail.next element to the current pointer
        # of the second list.
        if not curr1:
            tail.next = curr2
        else:
            tail.next = curr1
        
        return merged.next
            
        