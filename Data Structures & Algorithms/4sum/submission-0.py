class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # initialise quadruplets into an empty array
        quads = []
        # get the length of nums
        n = len(nums)
        # check if n is less than 4
        if n < 4:
            # return quads
            return quads
        # sort nums array
        nums.sort()
        # initialise pointer i to 0
        i = 0
        # loop through nums
        for i in range(n - 3):
            # check if nums[i] is the same as prev element
            if i > 0 and nums[i] == nums[i - 1]:
                # move on to the next loop
                continue
            for j in range(i + 1, n - 2):
                # check if nums[j] is the same as prev element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    # move on
                    continue
                # initialise left and right pointers
                l, r = j + 1, n - 1
                # converging pointers
                # while left is smaller than right
                while l < r:
                    # get the total of 4 pointers
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        # decrement right
                        r -= 1
                    elif total < target:
                        # increment left
                        l += 1
                    else:
                        # append into quads
                        quads.append([nums[i], nums[j], nums[l], nums[r]])
                        # increment left
                        l += 1
                        # decrement right
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            # increment left
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            # decrement right
                            r -= 1
        # return quads
        return quads
            