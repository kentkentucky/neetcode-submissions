class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # initialise left and right pointers
        # left at the start
        # right at the end
        l, r = 0, len(nums) - 1
        # initialise sort to an empty array
        sort = []
        # converge pointers
        while l <= r:
            # compute square of left and right element
            squarel = nums[l] ** 2
            squarer = nums[r] ** 2
            # check which squared element is larger
            # append accordingly
            if squarel > squarer:
                sort.insert(0, squarel)
                # increment left
                l += 1
            else:
                sort.insert(0, squarer)
                # decrement right
                r -= 1
        return sort
