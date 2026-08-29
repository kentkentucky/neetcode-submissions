class Solution:
    def minSwaps(self, s: str) -> int:
        # initialise close and max close to 0
        close = maxClose = 0
        # loop through s
        for i in s:
            # check for open bracket
            if i == "[":
                # decrement close
                close -= 1
            else:
                # increment close
                close += 1
            # update maxClose
            maxClose = max(close, maxClose)
        # return max swaps
        return (maxClose + 1) // 2