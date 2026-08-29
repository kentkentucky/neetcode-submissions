class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create object for s and t
        # loop through both words and count frequency of letters
        # compare object
        # return true if same
        # return false
        # time complexity = O(n)
        # space complexity = O(n^2)
        tallys = {}
        tallyt = {}
        for i in s:
            if (i in tallys):
                tallys[i] += 1;
            else:
                tallys[i] = 1;
        for i in t:
            if (i in tallyt):
                tallyt[i] += 1;
            else:
                tallyt[i] = 1;
        return tallys == tallyt;
        