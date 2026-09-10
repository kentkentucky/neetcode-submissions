class Solution:
    def countSubstrings(self, s: str) -> int:
        # get the length of s
        n = len(s)
        # initialise count to 0
        count = 0
        # loop till n
        for i in range(n):
            # even case
            # initialise left and right pointers
            l, r = i, i + 1
            # while left and right pointer in bound
            # while left elememt and right element equals
            while l >= 0 and r < n and s[l] == s[r]:
                # increment count
                count += 1
                # move pointer outwards
                # decrement l
                # increment right
                l -= 1
                r += 1

            # odd case
            # initialise left and right pointers
            l = r = i
            # while left and right pointer in bound
            # while left elememt and right element equals
            while l >= 0 and r < n and s[l] == s[r]:
                # increment count
                count += 1
                # move pointer outwards
                # decrement l
                # increment right
                l -= 1
                r += 1

        # return count
        return count