class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        condition:
        1) corner points appear only once and corner pts should be correct
        2) total area size must realized
        """
        points = []
        bag = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            # appearing once corner points
            pts = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
            for pt in pts:
                if pt in bag:
                    bag.remove(pt)
                else:
                    bag.add(pt)
            # calc area
            area += (x2 - x1) * (y2 - y1)

        # check corner points appear only once
        if len(bag) != 4:
            return False

        x1, y1, _, _ = min(rectangles, key=lambda p: (p[0], p[1]))
        _, _, x2, y2 = max(rectangles, key=lambda p: (p[2], p[3]))

        # check pts should be correct
        corner_pts = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
        for pt in corner_pts:
            if pt not in bag:
                return False
        return (x2 - x1) * (y2 - y1) == area
