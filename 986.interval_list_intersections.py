class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        ptr1 = ptr2 = 0
        N = len(firstList)
        M = len(secondList)
        while ptr1 < N and ptr2 < M:
            s1, e1 = firstList[ptr1]
            s2, e2 = secondList[ptr2]
            start = max(s1, s2)
            end = min(e1, e2)
            if end >= start:
                ans.append([start, end])
            if e1 < e2:
                ptr1 += 1
            else:
                ptr2 += 1
        return ans
