class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []
        self.min = None
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)

        if self.min is None or val < self.min:
            self.min = val
        self.smallest.append(self.min)

    def pop(self) -> None:
        
        self.stack.pop()
        self.smallest.pop()
        self.min = self.smallest[-1] if self.smallest else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
