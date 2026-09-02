class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initialise longest to 0
        longest = 0
        # initialise starting index to 0
        start = 0

        # loop through s
        for i in range(len(s)):
            # even case
            # initialise left and right pointers
            l, r = i , i + 1
            # move pointers outward
            # while in bound and matching
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if palindrome is longest
                if (r - l) + 1 > longest:
                    # update start index
                    start = l
                    # update length
                    longest = r - l + 1
                # move pointers outward
                r += 1
                l -= 1

            # odd case
            # initialise left and right pointers
            l = r = i
            # move pointers outward
            # while in bound and matching
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if palindrome is longest
                if (r - l) + 1 > longest:
                    # update start index
                    start = l
                    # update length
                    longest = r - l + 1
                # move pointers outward
                r += 1
                l -= 1

        # return longest palindrome substring
        return s[start:start + longest]