class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # initialise content to 0
        contented = 0
        # initialise two pointers to 0
        i = j = 0
        # sort both s and g
        s.sort()
        g.sort()
        # loop through s and g while in bound
        while i < len(s) and j < len(g):
            # check for same or larger size and greed
            if s[i] >= g[j]:
                # increment contented and j
                contented += 1
                j += 1
            # increment i
            i += 1
        # return content
        return contented