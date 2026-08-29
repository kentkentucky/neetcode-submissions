class Solution:
    def isHappy(self, n: int) -> bool:
        # initialise slow and fast
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            # move fast by 2 steps
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            # move slow by 1 step
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
        
    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output