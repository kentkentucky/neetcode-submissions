# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # initialise pointerA to headA
        pointerA = headA
        # initialise pointerB to headB
        pointerB = headB
        # loop while pointerA not equal pointerB
        while pointerA != pointerB:
            # move to the next node
            # assign pointerA to headB once reach the end of listA
            pointerA = pointerA.next if pointerA else headB
            # move to the next node
            # assign pointerB to headA once reach the end of listB
            pointerB = pointerB.next if pointerB else headA
        # return intersection node or null
        return pointerA