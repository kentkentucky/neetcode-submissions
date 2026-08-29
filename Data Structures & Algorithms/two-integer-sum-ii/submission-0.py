class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialise left and right pointers
        l, r = 0, len(numbers) - 1
        # converging pointers
        # loop while l is less than right
        while l < r:
            # check if left and right index element add up to target
            if numbers[l] + numbers[r] == target:
                # return the indexes
                return [l + 1, r + 1]
            # else if left and right elements is larger
            elif numbers[l] + numbers[r] > target:
                # decrement right
                r -= 1
            # else it would be lesser than target
            else:
                # increment left
                l += 1