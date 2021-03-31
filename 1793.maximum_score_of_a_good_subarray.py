class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = nums[k] * 1

        # pre-cal and calculate ans with right part
        curr = nums[k]
        for i in range(k + 1, N):
            nums[i] = min(curr, nums[i])
            curr = nums[i]
            ans = max(ans, curr * (i - k + 1))
        # pre-cal and calculate ans with left part
        curr = nums[k]
        for i in range(k - 1, -1, -1):
            nums[i] = min(curr, nums[i])
            curr = nums[i]
            ans = max(ans, curr * (k - i + 1))

        # two pointer to shrink
        l, r = 0, N - 1
        while l < k and r > k:
            curr = min(nums[l], nums[r])
            ans = max(ans, curr * (r - l + 1))
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return ans
