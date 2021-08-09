class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1.pop(0))
        value = self.queue1.pop(0)

        for _ in range(len(self.queue2)):
            self.queue1.append(self.queue2.pop(0))

        return value

    def top(self) -> int:
        """
        Get the top element.
        """
        for _ in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1.pop(0))
        value = self.queue1.pop(0)
        self.queue2.append(value)

        for _ in range(len(self.queue2)):
            self.queue1.append(self.queue2.pop(0))

        return value

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
