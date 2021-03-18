class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [start, end] = interval
        sort by start
        heap size => min # of room
        iter intervals
            1) if min end in heap <= current start => pop up from heap
            2) add current end to heap
            3) res = max(res, len(heap))

        """
        intervals.sort()
        heap = []
        res = 0
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            res = max(res, len(heap))
        return res
