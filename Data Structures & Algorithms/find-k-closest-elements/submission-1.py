class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # initialise left and right pointers
        l, r = 0, len(arr) - 1
        # loop while 
        while r - l >= k:
            # get the difference
            i = abs(arr[l] - x)
            j = abs(arr[r] - x)
            # check the difference
            if i > j:
                # increment left
                l += 1
            else:
                # decrement right
                r -= 1
        # return the closest elements
        return arr[l:r + 1]