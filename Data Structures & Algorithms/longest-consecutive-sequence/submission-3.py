class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums array to set
        numSet = set(nums)
        # initialise longest to 0
        longest = 0

        # loop through nums
        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest