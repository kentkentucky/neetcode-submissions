class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initialise left and right pointers
        l, r = 0, len(s) - 1
        # loop while left is less than right
        while l < r:
            # check for different characters
            if s[l] != s[r]:
                # skip left string
                skipL = s[l + 1 : r + 1]
                # skip right string
                skipR = s[l : r]
                # check if same string
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1
        # return true
        return True
