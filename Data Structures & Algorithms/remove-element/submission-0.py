class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialise k to 0
        k = 0
        # loop through nums
        for num in nums:
            # check if num is not equal to val
            if num != val:
                # update nums array at index k
                nums[k] = num
                # increment k
                k += 1
        # return k
        return k