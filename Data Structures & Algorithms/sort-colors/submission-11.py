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
            # check for 0
            if nums[k] == 0:
                # increment left
                l += 1
                # swap elements
                nums[l], nums[k] = nums[k], nums[l]
                # increment k
                k += 1
            # check for 2
            elif nums[k] == 2:
                # decrement right
                r -= 1
                # swap elements
                nums[r], nums[k] = nums[k], nums[r]
            else:
                # increment k
                k += 1