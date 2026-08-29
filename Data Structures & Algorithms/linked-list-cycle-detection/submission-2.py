# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # initialise tortoise and hare to the head of the list
        t = h = head
        # loop while tortoise and hare are not null
        while h and h.next:
            # increment tortoise by a step
            t = t.next
            # increment hare by two steps
            h = h.next.next
            # check if tortoise and hare are the same
            # cycle indication
            if t == h:
                # return true
                return True
        # return false
        return False