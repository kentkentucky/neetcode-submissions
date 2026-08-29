class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # initialise left and right pointer
        l, r = 0, len(nums) - 1
        # converging pointers
        while l < r:
            if nums[l] % 2 != 0 and nums[r] % 2 != 1:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 != 0:
                r -= 1
        return nums