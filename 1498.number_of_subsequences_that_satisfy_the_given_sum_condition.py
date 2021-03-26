class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        sort: O(NlogN)
        sliding window: O(N)

        a b c d =>
        l -> : only add count for each different l value
        r ->

        a       = a                                  = 1
        a b     = a b                                = 2^0
        a b c   = a b c, a _ c                       = 2^1
        a b c d = a b c d, a b _ d, a _ c d, a _ _ d = 2^2
        1 + 2^0 + 2^1 + 2^2 = 2^3
        => combination = 2^(j-i)

        time complexity: O(NlogN + N)
        """
        nums.sort()
        N = len(nums)
        mod = 10**9 + 7
        l, r = 0, N - 1
        ans = 0
        while l <= r:
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            if l <= r:
                ans += pow(2, max(r - l, 0), mod)  # 1 if (r - l) < 0 else 2^(r-l)
                l += 1

        return ans % mod
