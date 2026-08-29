class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # initialise left and right pointers
        l, r = 0, len(s) - 1
        # loop while left is less than right
        while l < r:
            # store right index element in temp
            temp = s[r]
            # update right index to left element
            s[r] = s[l]
            # update left index to temp
            s[l] = temp
            # increment left
            l += 1
            # decrement right
            r -= 1