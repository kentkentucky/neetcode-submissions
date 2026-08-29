class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get the length of nums
        n = len(nums)
        # reverse nums
        nums[:] = nums[::-1]
        # reverse the first k elements and the last n - k elements
        nums[:] = nums[:k % n][::-1] + nums[k % n:][::-1]