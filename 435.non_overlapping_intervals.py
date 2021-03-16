class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        sort by end, and then start
        dp to find max intervals incuding itself

        dp[i]
        j: interval from 0 to n-1
        i: interval from 0 to j-1

        initialization = 1 for all

        dp[i] = 
            if intervals[j].start >= intervals[i].end:
                max(dp[j], dp[i] + 1)

        ans = total intervals - max_intervals
        """
        if not intervals:
            return 0
        n = len(intervals)
        intervals.sort(key=lambda x: (x[1], x[0]))
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if intervals[i][1] <= intervals[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
                else:
                    break
        return n - max(dp)
