class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # initialise pointers for s and t
        i = j = 0
        # get the length of s and t
        n = len(s)
        m = len(t)
        # loop while i and j are in bound
        while i < n and j < m:
            if s[i] == t[j]:
                # increment i
                i += 1
                # increment j
                j += 1
            else:
                i += 1
        return m - j