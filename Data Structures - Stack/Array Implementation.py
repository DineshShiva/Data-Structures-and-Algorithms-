class Stack:
    def __init__(self):
        self.list = []

    def push(self,data):
        self.list.append(data)

    def pop(self):
        self.list.pop()

    def peek(self):
        return self.list[-1]

    def display(self):
        for i in range(len(self.list)-1,-1,-1):
            print(self.list[i])


myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)

myStack.display()

myStack.pop()
myStack.pop()

print("\n")
myStack.display()

print("\n")
print(str(myStack.peek()))
