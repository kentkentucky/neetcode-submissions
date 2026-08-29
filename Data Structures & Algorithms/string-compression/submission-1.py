class Solution:
    def compress(self, chars: List[str]) -> int:
        # initialise pointer i to 0
        i = 0
        # initialise write pos to 0
        k = 0
        # get the length of chars
        n = len(chars)
        # loop through chars using pointer i
        while i < n:
            # initialise pointer j to next index of i
            j = i + 1
            # while j in bound
            # while chars[i] is equal to chars[j]
            while j < n and chars[i] == chars[j]:
                # increment pointer j
                j += 1
            # write the char to position k in chars
            chars[k] = chars[i]
            # increment write position
            k += 1
            # check if count is more than one
            if j - i > 1:
                # convert count to str
                count = str(j - i)
                # loop through str
                for c in count:
                    # write element into write position
                    chars[k] = c
                    # increment write position
                    k += 1
            # move pointer to index j
            i = j
        # return write position
        return k
                    
