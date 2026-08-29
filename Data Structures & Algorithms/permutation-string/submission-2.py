class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get the length of s1
        n = len(s1)
        # get length of s2
        m = len(s2)

        # check if s1 is longer than s2
        if n > m:
            # return false
            return False

        # make s1 a dict
        s1D = Counter(s1)
        # make a dict of len n for s2
        s2D = Counter(s2[:n])

        # check for permutation
        if s1D == s2D:
            # return true
            return True

        # loop from n to m
        for i in range(n, m):
            # add new char to s2D
            s2D[s2[i]] += 1
            # remove old char from window
            s2D[s2[i - n]] -= 1

            # remove key
            if s2D[s2[i - n]] == 0:
                del s2D[s2[i - n]]

            # check for permutation
            if s1D == s2D:
                # return true
                return True

        # return false
        return False