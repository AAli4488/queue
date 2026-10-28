# LeetCode Queue & Stack Problems (Python)

Python solutions for two classic LeetCode problems on implementing one data structure using the other.

| # | Title | Difficulty | Link |
|---|-------|------------|------|
| 232 | Implement Queue using Stacks | Easy | [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) |
| 225 | Implement Stack using Queues | Easy | [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/) |

---

## 232. Implement Queue using Stacks

### Problem
Build a first-in-first-out (FIFO) queue using only **two stacks**. The queue must support:

- `push(x)` - add element `x` to the back of the queue
- `pop()` - remove and return the element at the front
- `peek()` - return the front element without removing it
- `empty()` - return `True` if the queue is empty

**Follow-up:** make every operation amortized O(1).

### Example
```
q = MyQueue()
q.push(1)
q.push(2)
q.peek()   # 1
q.pop()    # 1
q.empty()  # False
```

### Approach
Use two stacks:

- `in_stack` receives all new pushes.
- `out_stack` serves `pop` and `peek`.

When `out_stack` is empty, move everything from `in_stack` into it. This reverses the order, so the oldest element ends up on top. Each element is moved at most once, which gives amortized O(1).

### Solution
```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```

### Complexity
| Operation | Time |
|-----------|------|
| push | O(1) |
| pop / peek | O(1) amortized |
| empty | O(1) |

Space: O(n)

---

## 225. Implement Stack using Queues

### Problem
Build a last-in-first-out (LIFO) stack using only **queue operations** (push to back, pop/peek from front, size, is-empty). The stack must support:

- `push(x)` - push element `x` onto the stack
- `pop()` - remove and return the top element
- `top()` - return the top element
- `empty()` - return `True` if the stack is empty

### Example
```
s = MyStack()
s.push(1)
s.push(2)
s.top()    # 2
s.pop()    # 2
s.empty()  # False
```

### Approach
Use a single queue. After each `push`, rotate the queue so the newest element moves to the front. The front of the queue is then always the top of the stack.

### Solution
```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
```

### Complexity
| Operation | Time |
|-----------|------|
| push | O(n) |
| pop / top / empty | O(1) |

Space: O(n)

---

## Run locally
```python
q = MyQueue()
q.push(1); q.push(2)
print(q.peek(), q.pop(), q.empty())   # 1 1 False

s = MyStack()
s.push(1); s.push(2)
print(s.top(), s.pop(), s.empty())    # 2 2 False
```

## References
- [Python solutions repo (225 & 232)](https://github.com/ashishkssingh/Leetcode-Python)
- [232 write-up](https://github.com/wind-liang/leetcode/blob/master/leetcode-232-Implement-Queue-using-Stacks.md)
- [225 write-up](https://github.com/tech-cow/leetcode/commit/2e6dd3d456b639544fa57e7acada55cf6e80b4a9)