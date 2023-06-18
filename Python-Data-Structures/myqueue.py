# Queue implementation indd Python
# It can also be implemented using linked list

class Queue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = -1
        self.rear = -1
        self.queue = [None] * size

    def isFull(self):
        return self.count == self.size - 1
    
    def isNull(self):
        return self.front == -1

    def enqueue(self, value):

        if self.isNull():
            self.front += 1
            self.rear += 1
            self.queue[self.front] = value
        else:
            self.queue[self.rear]



