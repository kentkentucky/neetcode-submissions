# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialise a dummy node pointing to the head
        dummy = ListNode(next=head)
        # initialise fast and slow pointer to dummy
        fast = slow = dummy
        # move fast pointer n times
        for _ in range(n + 1):
            if fast:
                fast = fast.next
        # loop while fast is pointing to a node
        while fast:
            # move both fast and slow pointer to next node
            fast = fast.next
            slow = slow.next
        # check if slow.next.next exists
        if slow.next.next:
            # skip the next node
            slow.next = slow.next.next
        else:
            # assign next node to None
            slow.next = None
        # return head
        return dummy.next