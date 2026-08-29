class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialise write position to 0
        k = 0
        # initialise pointer i to 0
        i = 0
        # get the length of nums
        n = len(nums)
        # loop while i in bound of n
        while i < n:
            # initialise j to i + 1
            j = i + 1
            nums[k] = nums[i]
            k += 1
            while j < n and nums[i] == nums[j]:
                j += 1
                if j <= i + 2:
                    nums[k] = nums[i]
                    k += 1
            i = j
        # return k
        return k