class Solution:
    # pattern to get alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9]')
    def isPalindrome(self, s: str) -> bool:
        # lower case string and only retain alphanumeric characters
        cleaned = self.pattern.sub("", s.lower())
        # create left and right pointers
        left = 0
        right = len(cleaned) - 1
        # loop while left is not more than or equal right
        while left < right:
            # check for different characters
            if cleaned[left] != cleaned[right]:
                # return false
                return False
            # increment left
            left += 1
            # decrement right
            right -= 1
        return True
        