class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialise k to 0
        k = 0
        # get the length of nums
        n = len(nums)
        # loop through nums
        for i in range(n):
            if k == 0 or nums[i] != nums[i - 1]:
                # assign nums[i] at position k
                nums[k] = nums[i]
                # increment k
                k += 1
        # return k
        return k
        




