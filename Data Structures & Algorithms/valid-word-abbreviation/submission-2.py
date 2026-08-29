class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # initialise pointers and accumulator to 0
        i = j = skip = 0
        # get length of both word and abbr
        w = len(word)
        a = len(abbr)
        # loop through word while in bound
        while i < w and j < a:
            # check if abbr[j] is a digit
            if abbr[j].isdigit():
                # check if abbr[j] is 0 and x is 0
                if abbr[j] == '0' and skip == 0:
                    # return false
                    return False
                # add to skip count
                skip = skip * 10 + int(abbr[j])
            else:
                # increment i by skip count
                i += skip
                # initialise skip count back to 0
                skip = 0
                # check word index with word length
                # and matching char in word and abbr
                if i >= w or word[i] != abbr[j]:
                    # return false
                    return False
                # increment word pointer
                i += 1
            # increment abbr pointer
            j += 1
        # return results of comparison
        # word index + skip vs word length
        # abbr index vs abbr length
        return i + skip == w and j == a

