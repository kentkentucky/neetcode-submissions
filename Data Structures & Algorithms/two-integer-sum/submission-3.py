class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash table for seen
        seen = {}
        # loop through list 
        for i, num in enumerate(nums):
            # get diff
            diff = target - num;
            # lookup hash map for number
            if (diff in seen):
                return [seen[diff], i]
            seen[num] = i
        # time complexity = O(n)
        # space complexity = O(n)
