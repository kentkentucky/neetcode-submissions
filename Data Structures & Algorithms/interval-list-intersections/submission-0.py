class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # initialise intersection to an empty array
        intersection = []
        # initialise pointer i and j to 0
        i = j = 0

        # loop through the list
        while i < len(firstList) and j < len(secondList):
            # extract start1 and end1 from firstList[i]
            s1, e1 = firstList[i]
            # extract start2 and end2 from secondList[j]
            s2, e2 = secondList[j]

            # get the larger start point of s1, s2
            largerS = max(s1, s2)
            # get the smaller end point of e1, e2
            smallerE = min(e1, e2)
            
            # check if start smaller than or equal end
            if largerS <= smallerE:
                # append to intersection
                intersection.append([largerS, smallerE])

            # increment smaller end
            if e1 < e2:
                i += 1
            else:
                j += 1

        # return intersection
        return intersection