class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, 0))  # close is False
            events.append((r, h, 1))  # close is True
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        x, neg_h, _ = events[0]
        hp = Heap(-neg_h)
        ans = [[x, -neg_h]]
        for x, h, close in events[1:]:
            if close == 1:
                height = h
                hp.remove(height)
                if height > hp.max():
                    ans.append([x, hp.max()])
            else:
                height = -h
                if height > hp.max():
                    ans.append([x, height])
                hp.push(height)
        return ans


class Heap:
    def __init__(self, h=None):
        if h == None:
            self.hp = []
        else:
            self.hp = [-h]
        self.del_list = defaultdict(int)

    def push(self, val):
        heapq.heappush(self.hp, -val)

    def pop(self):
        self.__clear_up__()
        return -heapq.heappop(self.hp)

    def remove(self, val):
        self.del_list[val] += 1
        self.__clear_up__()


    def max(self):
        if not self.hp:
            return 0
        self.__clear_up__()
        return -self.hp[0]

    def __clear_up__(self):
        # remove root marked as removed
        val = -self.hp[0]
        while self.del_list[val] > 0:
            heapq.heappop(self.hp)
            self.del_list[val] -= 1
            if not self.hp:
                break
            val = -self.hp[0]
