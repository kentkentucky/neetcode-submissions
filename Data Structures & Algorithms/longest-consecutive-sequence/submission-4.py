class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums array to set
        numSet = set(nums)
        # initialise longest to 0
        longest = 0

        # loop through nums
        for num in nums:
            # check if num is the beginning of sequence
            if num - 1 not in numSet:
                # initialise length to 0
                length = 0
                # check num + length exists in numSet
                while num + length in numSet:
                    # increase by 1
                    length += 1
                # get the longest sequence
                longest = max(length, longest)
        # return longest
        return longest