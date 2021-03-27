class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        2 4 5 8 10
        ^
        4 6 8 9
        ^

        if curr in both nums1 and nums2:
            val = curr + max(dp[ptr1-1], dp[ptr2-1])
            dp1[ptr1] = val
            dp2[ptr2] = val
            ptr1 += 1
            ptr2 += 1
        else:
            take smaller one to update its dp
            dp[ptr] = curr + dp[ptr-1]
            ptr += 1
        """
        if nums1[-1] > nums2[-1]:
            nums1, nums2 = nums2, nums1
        N = len(nums1) + 1
        M = len(nums2) + 1
        MOD = 10**9 + 7
        dp1 = [0] * N
        dp2 = [0] * M
        ptr1 = ptr2 = 1
        while ptr1 < N or ptr2 < M:
            if ptr1 < N and ptr2 < M and nums1[ptr1 - 1] == nums2[ptr2 - 1]:
                curr = nums1[ptr1 - 1]
                val = curr + max(dp1[ptr1 - 1], dp2[ptr2 - 1])
                dp1[ptr1] = val % MOD
                dp2[ptr2] = val % MOD
                ptr1 += 1
                ptr2 += 1
            else:
                if ptr1 == N or nums1[ptr1 - 1] > nums2[ptr2 - 1]:
                    # update ptr2
                    dp2[ptr2] = (nums2[ptr2 - 1] + dp2[ptr2 - 1])
                    ptr2 += 1
                else:
                    # update ptr1
                    dp1[ptr1] = nums1[ptr1 - 1] + dp1[ptr1 - 1]
                    ptr1 += 1
        return max(dp1[-1], dp2[-1]) % MOD
