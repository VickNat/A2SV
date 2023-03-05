class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.k = k
        self.front = -1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.front == -1:
                self.front = 0
                self.rear = 0
            elif self.front == 0:
                self.front = self.k-1
            else:
                self.front -= 1
            
            self.queue[self.front] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.front == -1:
                self.front = 0
                self.rear = 0
            elif self.rear == self.k-1:
                self.rear = 0
            else:
                self.rear += 1
            
            self.queue[self.rear] = value
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front == self.k-1:
                self.front = 0
            else:
                self.front += 1
            
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.rear == 0:
                self.rear = self.k-1
            else:
                self.rear -= 1

            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty() or self.rear < 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.front == 0 and self.rear == self.k-1) or (self.rear+1 == self.front):
            return True
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