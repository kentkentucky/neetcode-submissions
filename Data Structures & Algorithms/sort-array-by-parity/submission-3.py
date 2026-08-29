class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # initialise left and right pointer
        l, r = 0, len(nums) - 1
        # converging pointers
        while l < r:
            # check if left and right elements can be swapped
            if nums[l] % 2 != 0 and nums[r] % 2 != 1:
                # swap left and right elements
                nums[l], nums[r] = nums[r], nums[l]
            # check for even number
            if nums[l] % 2 == 0:
                # increment left
                l += 1
            # check for odd number
            if nums[r] % 2 != 0:
                # decrement right
                r -= 1
        # return nums
        return nums