class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_len = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.max_len
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue[self.front] is not None:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max_len
            return True
        else:
            return False

    def Front(self) -> int:
        if self.queue[self.front] is None:
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.queue[self.rear - 1] is None:
            return -1
        else:
            return self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.queue[self.front] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.queue[self.front] is not None:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
