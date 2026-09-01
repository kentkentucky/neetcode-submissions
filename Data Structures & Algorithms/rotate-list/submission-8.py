# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases
        if not head or not head.next:
            return head

        # count nodes
        # initialise count to 0
        count = 0
        # assign curr to head
        curr = head
        # loop while curr pointing to a node
        while curr:
            # move to the next node
            curr = curr.next
            # increment count
            count += 1

        # edge case
        # mod k by count
        k %= count
        if k == 0:
            return head

        # initialise slow and fast pointer to head
        slow = fast = head
        # move the fast pointer k % count times
        for _ in range((k % count) + 1):
            # move to the next node
            fast = fast.next

        # loop while fast is pointing to a node
        while fast:
            # move to the both fast and slow to the next node
            fast = fast.next
            slow = slow.next

        # save new head
        head2 = curr2 = slow.next
        # point slow.next to null
        slow.next = None

        while curr2 and curr2.next:
            curr2 = curr2.next
        curr2.next = head

        return head2