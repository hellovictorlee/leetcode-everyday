class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int],
                     X: int) -> int:
        """
        [1,0,1,2,1,1,7,5]
        [0,1,0,1,0,1,0,1]
        |     |
        1) calc orgin #
        2) slide window to track max #
        """
        N = len(customers)
        tot = 0
        for cu, gr in zip(customers, grumpy):
            if gr == 0:
                tot += cu

        for i in range(X):
            if grumpy[i] == 1:
                tot += customers[i]
        res = tot
        for i in range(X, N):
            if grumpy[i - X] == 1:
                tot -= customers[i - X]
            if grumpy[i] == 1:
                tot += customers[i]
            res = max(res, tot)
        return res
