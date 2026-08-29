class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # define pointers for both string
        i = j = 0
        # loop through while both pointers does that exceed boundaries
        while i < len(s) and j < len(t):
            # check for same character
            if s[i] == t[j]:
                # increment i
                i += 1
            # increment j
            j += 1
        # return true or false according to i == len(s)
        return i == len(s)
