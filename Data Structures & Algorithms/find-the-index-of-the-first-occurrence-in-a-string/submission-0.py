class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # get the length of haystack and needle
        h = len(haystack)
        n = len(needle)
        # loop through haystack
        for i in range(h):
            # use fixed window to check
            if needle == haystack[i:i + n]:
                # return index
                return i
        # not part of haystack
        # return -1 
        return -1