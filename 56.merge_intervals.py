# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = []
        curr_start, curr_end = intervals[0]
        for start, end in intervals[1:]:
            if curr_end >= start:
                curr_end = max(curr_end, end)
            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = start, end
        res.append([curr_start, curr_end])
        return res
