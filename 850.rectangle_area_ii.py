class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        time complexity: O(N + NlogN + N * NlogN) = O(N^2 * logN)
        """
        MOD = 1000000007

        # create sweep lines events
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))  # 1 stand for opening
            events.append((x2, 0, y1, y2))  # 0 stand for closing
        events.sort(key=lambda x:
                    (x[0], -x[1]))  # closing should be earlier than opening

        # create helper function (sweep lines) for area
        def rangeArea(width, lines):
            if not lines:
                return 0
            lines.sort()
            height = 0
            curr_y1, curr_y2 = lines[0]
            for y1, y2 in lines[1:]:
                if y1 > curr_y2:
                    height += curr_y2 - curr_y1
                    curr_y1, curr_y2 = y1, y2
                else:
                    curr_y2 = max(curr_y2, y2)
            height += curr_y2 - curr_y1
            return width * height

        lines = []
        prev_x = -float('inf')
        area = 0
        for x, close, y1, y2 in events:
            width = x - prev_x
            area += rangeArea(width, lines)
            prev_x = x
            if close == 0:
                lines.remove((y1, y2))
            else:
                lines.append((y1, y2))

        return area % MOD
