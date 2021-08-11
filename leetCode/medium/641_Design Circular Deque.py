class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.d = collections.deque()
        self.max_len = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.d) < self.max_len:
            self.d.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.d) < self.max_len:
            self.d.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.d) == 0:
            return False
        else:
            self.d.popleft()
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.d) == 0:
            return False
        else:
            self.d.pop()
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.d) == 0:
            return -1
        else:
            return self.d[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.d) == 0:
            return -1
        else:
            return self.d[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.d) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.d) == self.max_len:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
