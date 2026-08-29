class Solution:
    def isHappy(self, n: int) -> bool:
        # initialise visited to a empty set
        # keep track of the numbers visited
        visited = set()
        # loop while n is not 1 and n not in visited
        while n != 1 and n not in visited:
            # add current number to visited
            visited.add(n)
            # initialise sum to 0
            sum = 0
            # loop while n is not 0
            while n > 0:
                # extract last digit
                n, digit = divmod(n, 10)
                # add to sum the squared number
                sum += digit ** 2
            # update n 
            n = sum
        # return true if we reach 1
        # return false if we found a cycle
        return n == 1