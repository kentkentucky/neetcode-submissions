class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialise maximum area to 0
        maxArea = 0
        # initialise left and right pointers
        l, r = 0, len(heights) - 1
        # converging pointers
        while l < r:
            # calculate area of container
            area = min(heights[l], heights[r]) * (r - l)
            # compare and assign nex max
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        # return maxArea
        return maxArea