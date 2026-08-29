class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialise triplets to an empty array
        trips = []
        # get the length of nums
        n = len(nums)
        # initialise pointer i to 0
        i = 0
        # sort nums
        nums.sort()
        # loop through nums
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # initialise left and right pointers
            l, r = i + 1, n - 1
            # loop while left is less than right:
            while l < r:
                # check if they add up to 0
                if nums[i] + nums[l] + nums[r] == 0:
                    # append to triplets array
                    trips.append([nums[i], nums[l], nums[r]])
                    # increment left
                    l += 1
                    # decrement right
                    r -= 1
                    # skip duplicates for second element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicates for third element
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                # check if they are larger than 0
                elif nums[i] + nums[l] + nums[r] > 0:
                    # decrement right
                    r -= 1
                # else they would be less than 0
                else:
                    # increment left
                    l += 1
            # increment i
            i += 1
        # return trips
        return trips