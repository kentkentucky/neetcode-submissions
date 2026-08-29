class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # initialise pointers for word1 and word2
        i = j = 0
        # get the length of both word1 and word2
        m = len(word1)
        n = len(word2)
        # initialise merged to an empty string
        merged = ""
        # loop through word1 and word2 while still in bound
        while i < m and j < n:
            # append char from word1
            merged += word1[i]
            # append char from word2
            merged += word2[j]
            # increment both pointers
            i += 1
            j += 1
        # add remaining char
        # return merged string
        return merged + word1[i:m] + word2[j:n]