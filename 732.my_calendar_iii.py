class MyCalendarThree:

    def __init__(self):
        self.count = Counter()
        

    def book(self, start: int, end: int) -> int:
        self.count[start] += 1
        self.count[end] -= 1

        room = 0
        ans = 0
        for time in sorted(self.count.keys()):
            room += self.count[time]
            ans = max(ans, room)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
