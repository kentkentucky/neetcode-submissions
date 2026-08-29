# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialise slow and fast pointers
        fast = head
        slow = head
        # loop through list while fast is in bound / not null
        while fast and fast.next:
            # increment fast by 2 steps
            fast = fast.next.next
            # increment slow
            slow = slow.next
        # return slow pointer
        return slow