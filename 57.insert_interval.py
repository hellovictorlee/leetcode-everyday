class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        """
        1) find i to insert
        2) iterate intervals
        """
        start, end = newInterval
        ptr = 0
        N = len(intervals)
        while ptr < N:
            s, e = intervals[ptr]
            if start <= s:
                intervals.insert(ptr, newInterval)
                break
            ptr += 1
        if len(intervals) == N:
            intervals.append(newInterval)

        ans = []
        curr_s, curr_e = intervals[0]
        for s, e in intervals:
            if curr_e < s:
                ans.append([curr_s, curr_e])
                curr_s, curr_e = s, e
            else:
                curr_e = max(curr_e, e)
        ans.append([curr_s, curr_e])
        return ans
