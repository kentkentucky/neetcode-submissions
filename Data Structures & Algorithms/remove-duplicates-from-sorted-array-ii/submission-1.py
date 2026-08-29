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
            # write nums[i] to write position k
            nums[k] = nums[i]
            # increment write position
            k += 1
            # loop while j is in bound
            # if nums[i] and nums[j] is the same
            while j < n and nums[i] == nums[j]:
                # increment j
                j += 1
                # check if j is in window of 2
                if j <= i + 2:
                    # write nums[i] to write position k
                    nums[k] = nums[i]
                    # increment k
                    k += 1
            # move pointer i to index j
            i = j
        # return k
        return k