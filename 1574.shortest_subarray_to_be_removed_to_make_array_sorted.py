class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        The key is to find the longest non-decreasing subarray starting with
        the first element or ending with the last element, respectively.

        [1,2,3,10,4,2,3,5]
                ^   ^
                l   r
        """
        N = len(arr)
        l, r = 0, N - 1

        # find l
        tmp = 0
        while l < N:
            if arr[l] >= tmp:
                tmp = arr[l]
                l += 1
            else:
                break
        l -= 1

        # find r
        tmp = 1000000000
        while r >= 0:
            if arr[r] <= tmp:
                tmp = arr[r]
                r -= 1
            else:
                break
        r += 1

        if l >= r:
            return 0

        # move l and r to find fulfilled condition
        # arr[l] <= arr[r]
        ans = min(r, N - l - 1)
        i, j = 0, r
        while i < l + 1 and j < N:
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans
