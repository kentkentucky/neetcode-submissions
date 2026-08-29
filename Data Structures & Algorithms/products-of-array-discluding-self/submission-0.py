class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # array for output
        output = []
        # initialise prefix
        pre = 1
        # loop through nums
        for i in nums:
            # store prefix accordingly
            output.append(pre)
            # update prefix
            pre *= i
        # initialise postfix
        post = 1
        # loop through nums in reverse
        for i in range(len(nums) - 1, -1, -1):
            # multiple prefix and postfix
            output[i] *= post
            # update postfix
            post *= nums[i]
        # return output
        return output