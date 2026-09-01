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
            i = i.parent
            if not i:
                i = q
            j = j.parent
            if not j:
                j = p
            if i == j:
                return i