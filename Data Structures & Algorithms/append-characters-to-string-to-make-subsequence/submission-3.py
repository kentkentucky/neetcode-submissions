class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # initialise pointers for s and t
        i = j = 0
        # get the length of s and t
        n = len(s)
        m = len(t)
        # loop while i and j are in bound
        while i < n and j < m:
            # check for same characters
            if s[i] == t[j]:
                # increment i
                i += 1
                # increment j
                j += 1
            else:
                # increment i 
                i += 1
        # return the number of characters needed to append to s
        return m - j