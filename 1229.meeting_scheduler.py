class Solution:
    def minAvailableDuration(self, slots1: List[List[int]],
                             slots2: List[List[int]],
                             duration: int) -> List[int]:
        """
        sort based on start

        ptr1: 0 -> len(slot1) - 1
        ptr2: 0 -> len(slot2) - 1

        condition:
        start = max(start1, start2)
        end = min(end1, end2)
        duration > end - start
        otherwise:
        1) move ptr1 if ptr1.end < ptr2.end
        2) other
        """
        slots1.sort()
        slots2.sort()
        ptr1, ptr2 = 0, 0
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            s1, e1 = slots1[ptr1]
            s2, e2 = slots2[ptr2]
            start = max(s1, s2)
            end = min(e1, e2)
            if duration <= end - start:
                return [start, start + duration]
            if e1 < e2:
                ptr1 += 1
            else:
                ptr2 += 1
        return []
