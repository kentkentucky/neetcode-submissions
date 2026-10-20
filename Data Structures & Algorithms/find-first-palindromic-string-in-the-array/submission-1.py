class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pass
        # loop through words
        for i in words:
            # reverse the current word
            reverse = i[::-1]
            if i == reverse:
                return i
        # return empty string
        return ""