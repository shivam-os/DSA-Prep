#Stack implementation in Python
#It can also be implemented using linked list

class Stack:
    def __init__(self, size):
        self.size = size #To save the initial size of stack
        self.top = -1 #To track the position where top item is
        self.stack = [None] * size #Create a stack with None values

    #Return true if stack is empty
    def isEmpty(self):
        return self.top == -1
    
    #Push the given value in stack i.e. at the top
    def push(self, value):
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = value
        else:
            print("Stack overflow!")
    
    #Pop the value from stack i.e the topmost value
    def pop(self):
        if self.isEmpty():
            print("Stack underflow!")
        else:
            self.stack[self.top] = None
            self.top -= 1
    
    #Returns the topmost value of stack
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        
        return self.stack[self.top]
    
    #Prints the stack in top to bottom order
    def traverse(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])

