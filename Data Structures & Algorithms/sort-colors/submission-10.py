class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initialise left and right pointers
        l, r = -1, len(nums)
        # initialise k to 0
        k = 0
        # loop while k is in bound
        while k < r:
            if nums[k] == 0:
                l += 1
                nums[l], nums[k] = nums[k], nums[l]
                k += 1
            elif nums[k] == 2:
                r -= 1
                nums[r], nums[k] = nums[k], nums[r]
            else:
                k += 1