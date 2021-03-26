class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
            r
        o o o
        x o o x x
        x
          l
        """
        N = len(nums)
        l = 0
        ans = N + 1
        tot = 0
        for r in range(N):
            tot += nums[r]
            while tot >= s:
                ans = min(ans, r - l + 1)
                tot -= nums[l]
                l += 1
        return 0 if ans == N + 1 else ans
