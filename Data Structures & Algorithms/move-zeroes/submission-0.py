class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initialise two pointers to 0
        i = j = 0
        # get the length of the array
        n = len(nums) - 1
        # loop while i and j is in bound
        while i <= n:
            # check if nums[j] is a zero
            if nums[j] != 0:
                # increment j
                j += 1
            # check for non zero element
            # check if i is more than j
            if nums[i] != 0 and i > j:
                # swap the elements
                nums[i], nums[j] = nums[j], nums[i]
            # increment i
            i += 1
                

