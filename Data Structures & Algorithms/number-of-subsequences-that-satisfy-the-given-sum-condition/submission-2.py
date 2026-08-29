class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        # initialise right pointer to end of nums
        r = len(nums) - 1
        # initialise subsequences to 0
        subs = 0
        # define mod
        mod = 10 ** 9 + 7
        # loop through nums
        for l, num in enumerate(nums):
            # while left is less than right
            # and left element + right element is more than target
            while l <= r and num + nums[r] > target:
                # decrement right
                r -= 1
            # if left is less than right
            if l <= r:
                # add to subs by the power of 2
                subs += pow(2, r - l, mod)
                # mod subs
                subs %= mod
        # return subs
        return subs
