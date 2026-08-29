class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t) return false
        if (len(s) != len(t)): return False
        # create a array for tally
        tally = [0] * 26
        # loop through s and count frequency
        # loop through t and subtract if similar
        for char_s, char_t in zip(s, t):
            tally[ord(char_s) - ord('a')] += 1
            tally[ord(char_t) - ord('a')] -= 1
        # return false if object is not 0 else true
        return all(c == 0 for c in tally)
        