class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t) return false
        if (len(s) != len(t)): return False
        # create a object for tally
        tally = {}
        # loop through s and count frequency
        for i in s:
            if (i in tally):
                tally[i] += 1;
            else:
                tally[i] = 1;
        # loop through t and subtract if similar
        for i in t:
            if (i in tally):
                tally[i] -= 1;
            else:
                tally[i] = -1;
        # return false if object is not 0
        for value in tally.values():
            if (value != 0):
                return False;
        # return true
        return True
        