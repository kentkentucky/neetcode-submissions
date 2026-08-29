class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create object
        # loop through list
        # add count into object
        # if any count > 1 return true
        # return false
        # time complexity = O(n)
        # space complexity = O(n)
        tally = {};
        for i in nums:
            if(i in tally):
                return True
            else:
                tally[i] = 1;
        return False;
        