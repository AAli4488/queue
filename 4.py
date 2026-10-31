#1700. Number of Students Unable to Eat Lunch
from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        i = 0                      # index of the top sandwich
        skipped = 0                # students who passed in a row

        while q and skipped < len(q):
            if q[0] == sandwiches[i]:
                q.popleft()
                i += 1
                skipped = 0
            else:
                q.append(q.popleft())
                skipped += 1

        return len(q)  
