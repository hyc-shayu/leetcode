class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(x if x < self.min_stack[-1] else self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int or float:
        return self.min_stack[-1]
