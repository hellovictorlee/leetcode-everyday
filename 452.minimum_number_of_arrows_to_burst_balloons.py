class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        overlay: endB >= startA and endA >= startB
        sort by (start, -end)
        => iterate => will guarantee endB >= startA

        calculate # of overlapping
        record maxEnd and compare to current start
        """
        if not points:
            return 0
        points.sort(key=lambda x: (x[0], -x[1]))
        currentEnd = float('inf')
        count = 1
        for start, end in points:
            if start > currentEnd:
                count += 1
                currentEnd = end
            else:
                currentEnd = min(currentEnd, end)
        return count
