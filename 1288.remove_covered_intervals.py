class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        count = 0
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue
                [a, b] = intervals[i]
                [c, d] = intervals[j]
                if c <= a and b <= d:
                    count += 1
                    break
        return len(intervals) - count
