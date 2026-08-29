class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # get the length of nums
        n = len(nums)
        # initialise modified to an empty array
        modified = [0] * n
        # initialise positive write pointer to 0
        pos = 0
        # initialise negative write pointer to 1
        neg = 1
        # loop through nums
        for i in nums:
            # if positive
            if i >= 0:
                # write to positive index
                modified[pos] = i
                # increment positive write pointer by 2
                pos += 2
            # else i would be negative
            else:
                # write to negative index in modified
                modified[neg] = i
                # increment negative write pointer by 2
                neg += 2
        # return modified
        return modified
                
        