class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # define pointers for both string
        a, b = 0, 0
        # loop throough while b is less than length of s
        while b < len(t):
            # check if a equals length of s 
            if a >= len(s) - 1:
                # return true
                return True
            # check for same character
            if s[a] == t[b]:
                # increment both pointers
                a += 1
                b += 1
            else:
                # remove character from t
                t = t[:b] + t[b + 1:]
        # return false
        return False
