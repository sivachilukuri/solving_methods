from collections import deque

class Mystack:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
        # Rotate the queue so the last element added is at the front
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        return self.queue.popleft()
    
# execution
s = Mystack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())