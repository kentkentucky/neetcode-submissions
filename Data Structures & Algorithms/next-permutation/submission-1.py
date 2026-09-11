class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get the length of nums
        n = len(nums)
        # initialise i to n - 2
        i = n - 2

        # loop while i is more than 0
        # stop when i + 1 is more than i
        while i >= 0 and nums[i] >= nums[i + 1]:
            # decrement i
            i -= 1
        
        # execute this only if i is more than 0
        if i >= 0:
            # initialise j to n - 1
            j = n - 1
            while nums[j] <= nums[i]:
                # decrement j
                j -= 1
            # swap i and j
            nums[i], nums[j] = nums[j], nums[i]

        # initialise left and right pointers
        l, r = i + 1, n - 1
        # converge pointers
        while l < r:
            # swap l and r elements
            nums[l], nums[r] = nums[r], nums[l]
            # increment left
            l += 1
            # decrement right
            r -= 1
