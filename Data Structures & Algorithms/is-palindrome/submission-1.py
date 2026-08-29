class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create left and right pointers
        left = 0
        right = len(s) - 1
        # loop while left is not more than or equal right
        while left < right:
            # check left character is alphanumeric
            if not s[left].isalnum():
                # increment left
                left += 1
                # continue
                continue
            # check right character is alphanumeric
            if not s[right].isalnum():
                right -= 1
                continue
            # check for different characters
            if s[left].lower() != s[right].lower():
                # return false
                return False
            # increment left
            left += 1
            # decrement right
            right -= 1
        return True
        