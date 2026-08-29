class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # initialise left and right pointers
        l, r = 0, len(arr) - 1
        # loop while 
        while r - l >= k:
            # get the difference
            i = abs(arr[l] - x)
            j = abs(arr[r] - x)
            if i > j:
                l += 1
            else:
                r -= 1
        return arr[l:r + 1]