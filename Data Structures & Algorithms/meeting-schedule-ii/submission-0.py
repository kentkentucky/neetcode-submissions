"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # initialise room count and max room count to 0
        maximum = count = 0
        # separate start and end timings
        # sort them
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        # initialise start and end pointers to 0
        s = e = 0

        # loop through while s is in bound of intervals
        while s < len(intervals):
            # check if start is smaller than end
            if start[s] < end[e]:
                # incrememt count and s
                count += 1
                s += 1
            else:
                # decrement count
                count -= 1
                # increment end
                e += 1
            # get the mac conunt
            maximum = max(maximum, count)
        
        # return max room count
        return maximum
