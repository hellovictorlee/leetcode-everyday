class Solution:
    def removeInterval(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        start, end = toBeRemoved
        ptr = 0
        N = len(intervals)
        # find left part
        while ptr < N:
            s, e = intervals[ptr]
            if e >= start:
                break
            ptr += 1
        left = ptr

        if left == N:
            return intervals

        # find right part
        while ptr < N:
            s, e = intervals[ptr]
            if s >= end:
                break
            ptr += 1
        right = ptr

        if left == right:
            return intervals

        # find middle part if needed
        mid_intervals = []
        left_start = intervals[left][0]
        if left_start < start:
            mid_intervals.append([left_start, start])
        right_end = intervals[right - 1][1]
        if right_end > end:
            mid_intervals.append([end, right_end])

        return intervals[:left] + mid_intervals + intervals[right:]
