class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pass
        # get the length of nums
        n = len(nums)
        # loop n times
        for i in range(n - 1):
            # check if current index and next index element are the same
            if nums[i] == nums[i + 1]:
                # double left value
                nums[i] = nums[i] * 2
                # change right value to 0
                nums[i + 1] = 0

        # initialise k to 0
        k = 0
        # loop n times
        for i in range(n):
            if nums[i] != 0:
                # swap elements
                nums[k], nums[i] = nums[i], nums[k]
                # increment k
                k += 1
        
        # return nums
        return nums

        
        
         