# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # initialise maximum sum of twin to 0
        maxTwin = 0
        # reverse the linked list halfway through
        # initialise fast and slow pointer
        fast = slow = head
        # initialise left pointer to head
        l = head
        # loop while fast pointer is in bound
        while fast.next and fast.next.next:
            # increment fast pointer by 2 nodes
            fast = fast.next.next
            # increment slow pointer
            slow = slow.next
        # slow pointer should be at the halfway point of the node
        # store slow in curr
        curr = slow.next
        # cut off the linked list midpoint
        slow.next = None
        # initialis prev to None
        prev = None
        # loop while curr is in bound
        while curr:
            # use temp to store next node
            tmp = curr.next
            # point next node of current to prev
            curr.next = prev
            # store curr node to prev
            prev = curr
            # move curr to the temp/next node
            curr = tmp
        # now prev should be at the last node
        # loop while prev and left are in bound
        while prev and l:
            # calculate twin sum
            total = l.val + prev.val
            # store the higher sum on maxTwin
            maxTwin = max(total, maxTwin)
            # move both pointer inwards
            l = l.next
            prev = prev.next
        # return maxTwin
        return maxTwin