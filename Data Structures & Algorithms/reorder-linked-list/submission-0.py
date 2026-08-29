# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # initialise left pointer to head
        l = head
        # reverse the second half of the linked list
        # initialise slow and fast pointers
        slow = head
        fast = head
        # loop while fast.next and fast.next.next 
        # points to existing nodes
        while fast.next and fast.next.next:
            # increment fast by 2 nodes
            fast = fast.next.next
            # increment slow
            slow = slow.next
        # slow pointer should be at the middle of the list
        # initialise curr to slow.next
        curr = slow.next
        # sever the connection
        slow.next = None
        # initialise prev to null
        prev = None
        # loop while slow is pointing to exisitng list
        while curr:
            # assign tmp to next node
            tmp = curr.next
            # point next node to prev
            curr.next = prev
            # assign prev to slow
            prev = curr
            # move to the next node
            curr = tmp
        # prev should be at the last node and list reversed
        while prev and l:
            # assign temp to the left pointer's next node
            tmp = l.next
            # assign l.next to prev
            l.next = prev
            # move prev pointer to next node
            prev = prev.next
            # assign l.next.next to tmp
            l.next.next = tmp
            # move l pointer to tmp
            l = tmp