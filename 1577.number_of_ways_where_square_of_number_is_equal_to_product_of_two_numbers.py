class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        hashmap => (key, val) = (product, combination)

        time complexity = O(N^2 + M^2 + N + M)
        """
        def count(nums_a, nums_b):
            N = len(nums_a)
            hashmap = defaultdict(int)
            for i in range(N - 1):
                for j in range(i + 1, N):
                    hashmap[nums_a[i] * nums_a[j]] += 1
            count = 0
            for num in nums_b:
                count += hashmap[num * num]
            return count

        return count(nums1, nums2) + count(nums2, nums1)
