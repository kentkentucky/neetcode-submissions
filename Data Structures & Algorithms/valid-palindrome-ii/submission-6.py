class Solution:
    def validPalindrome(self, s: str) -> bool:
        # flag to track delete
        delete = True
        # reverse the string s
        reverse = s[::-1]
        # length of the string
        n = len(s)
        # initialise pointer
        i = 0
        # use a pointer to loop through s and reverse
        while i < n - 1:
            # if same character continue
            if s[i] == reverse[i]:
                # increment i 
                i += 1
            # check for different character
            # check if delete is available
            elif s[i] != reverse[i] and delete:
                if s[:n - i - 1] + s[n - i:] == reverse[:i] + reverse[i + 1:]:
                    s = s[:n - i - 1] + s[n - i:]
                    reverse = reverse[:i] + reverse[i + 1:]
                else:
                    s = s[:i] + s[i + 1:]
                    reverse = reverse[:n - i - 1] + reverse[n - i:]
                # assign delete to False
                delete = False
            else:
                return False
        return True