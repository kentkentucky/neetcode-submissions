"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # initialise pointer i to p
        i = p
        # initialise pointer j to q
        j = q
        # loop while True
        while True:
            # move to parent node
            i = i.parent
            # check if i is at the head 
            if not i:
                # point to node q
                i = q
            # move to parent node
            j = j.parent
            # check if j is at the head
            if not j:
                # move to node p
                j = p
            # check for intersection
            if i == j:
                # return lca node
                return i