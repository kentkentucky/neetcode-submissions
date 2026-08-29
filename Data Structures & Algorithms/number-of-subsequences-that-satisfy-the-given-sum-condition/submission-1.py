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
            while l <= r and num + nums[r] > target:
                r -= 1
            if l <= r:
                subs += pow(2, r - l, mod)
                subs %= mod
        return subs
