class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort people
        people.sort()
        # initialise number of boats to 0
        boats = 0
        # initialise left and right pointers
        l, r = 0, len(people) - 1
        # converging pointers
        # while left is less than right
        while l <= r:
            # increment boats
            boats += 1
            # only one person left
            if l == r:
                break
            # check if its overweight
            if people[l] + people[r] > limit:
                # the heaviest person allocated a boat
                # move right pointer down
                r -= 1
            # else equal or lesser than limit
            else:
                # both person takes the boat
                # move left pointer up
                l += 1
                # move right pointer down
                r -= 1
        # return boats
        return boats