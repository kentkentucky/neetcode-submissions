class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass
        # initialise pointers to the end of s and t
        i = len(s) - 1
        j = len(t) - 1
        # initialise skip to 0
        skipS = 0
        skipT = 0
        while i >= 0 or j >= 0:
            # loop backwards while i in bound
            while i >= 0:
                # check for #
                if s[i] != "#":
                    # check if skip is 0
                    if skipS == 0:
                        # break out
                        break
                    else:
                        # decrement skipS
                        skipS -= 1
                else:
                    # increment skipS
                    skipS += 1
                # decrement i
                i -= 1
            # loop backwards while j in bound
            while j >= 0:
                # check for #
                if t[j] != "#":
                    if skipT == 0:
                        break
                    else:
                        skipT -= 1
                else:
                    skipT += 1
                # decrement j
                j -= 1
            # check if any of the pointers are out of bounds
            if (i < 0) !=  (j < 0):
                # return false
                return False
            # check for same character
            if s[i] == t[j]:
                # decrement i and j
                i -= 1
                j -= 1
            else:
                # return false
                return False
        # return true
        return True