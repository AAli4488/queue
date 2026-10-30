#933. Number of Recent Calls
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        # drop requests older than 3000 ms
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
