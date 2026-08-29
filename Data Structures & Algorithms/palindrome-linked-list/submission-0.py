# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # initialise slow and fast pointers
        slow = head
        fast = head.next
        # loop till fast reach the end of the linked list
        while fast and fast.next:
            # increment fast by two steps
            fast = fast.next.next
            slow = slow.next

        # initialise previous to none
        prev = None
        # initialise curr to slow.next
        curr = slow.next
        # reverse the second half of the list
        while curr:
            # assign curr to temp
            temp = curr.next
            # assign curr.next to prev
            curr.next = prev
            # assign temp to prev
            prev = curr
            # move to the next node
            curr = temp

        # compare second half with first half
        # loop through second half
        while prev:
            # check for different element
            if prev.val != head.val:
                # return false
                return False
            prev = prev.next
            head = head.next
        # return true
        return True

