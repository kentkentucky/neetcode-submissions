class Solution:
    def isHappy(self, n: int) -> bool:
        # initialise slow and fast
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            # move fast by 2 steps
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            # move slow by 1 step
            slow = self.sumOfSquares(slow)
        # return the result of a cycle
        return True if fast == 1 else False
        
    # helper function to compute the sum of squares
    def sumOfSquares(self, n: int) -> int:
        # initialise output to 0
        output = 0
        # loop while n is more than 0
        while n:
            # get the last digit
            digit = n % 10
            # square digit
            # add to output
            output += digit ** 2
            # remove the last digit
            n = n // 10
        # return output
        return output