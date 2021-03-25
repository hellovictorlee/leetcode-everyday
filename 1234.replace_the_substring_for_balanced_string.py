class Solution:
    def balancedString(self, s: str) -> int:
        """
            i
        x o o x x
          j
        """
        N = len(s)
        counter = Counter(s)
        ans = N
        j = 0
        # j: left part
        # i: right part
        for i, c in enumerate(s):
            counter[c] -= 1
            while j < N and all([val <= N / 4 for val in counter.values()]):
                ans = min(ans, i - j + 1)
                counter[s[j]] += 1
                j += 1
        return ans
