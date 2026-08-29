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
            if i >= 0:
                modified[pos] = i
                pos += 2
            else:
                modified[neg] = i
                neg += 2
        return modified
                
        