"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        maxRoomNeeded = 0
        currRoomOccupied = 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] < end[j]:
                i += 1
                currRoomOccupied += 1
            else:
                j += 1
                currRoomOccupied -= 1
            maxRoomNeeded = max(maxRoomNeeded, currRoomOccupied)
        return maxRoomNeeded