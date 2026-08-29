class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # initialise content to 0
        contented = 0
        # initialise two pointers to 0
        i = j = 0
        # sort both s and g
        s.sort()
        g.sort()
        # loop through s
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                contented += 1
                j += 1
            elif s[i] > g[j]:
                j += 1
            i += 1
        # return content
        return contented