class Solution:
    def reverseWords(self, s: str) -> str:
        pass
        # initialise reverse to an empty string
        reverse = ""
        # initialise two pointer to 0
        i = j = 0
        while i < len(s) and j < len(s):
            # if element is not space
            if s[j] != " ":
                # increment j
                j += 1
            else:
                # append reversed string into reverse
                reverse += s[i:j][::-1] + " "
                i = j = j + 1
        # return reverse + reverse of remaining string
        return reverse + s[i:j][::-1]
                