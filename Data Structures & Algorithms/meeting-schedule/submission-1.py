"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals = sorted(intervals, key=lambda interval: interval.start)
        for i in range(n):
            if n > i+1 and intervals[i].end > intervals[i+1].start:
                return False
        return True