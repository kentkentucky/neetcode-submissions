class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # initialise charLast to hash map
        charLast = {}
        # loop through the s backwards
        # store the last index of each character
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in charLast:
                charLast[s[i]] = i
        # initialise sizes to an empty array
        sizes = []
        # initialise size and end to 0
        size = end = 0
        for i, c in enumerate(s):
            # increment size
            size += 1
            # get the end base on char
            end = max(end, charLast[c])

            # check if we reach the end
            if i == end:
                # append size to sizes
                sizes.append(size)
                # reset counters
                size = end = 0
        # return sizes
        return sizes
            
