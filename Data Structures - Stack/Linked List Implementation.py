class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0


    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = self.bottom = new_node
            self.length = +1

        else:
            new_node.next = self.top
            self.top = new_node
            self.length +=1

    def pop(self):
        if self.length == 0:
            print("Stack is Empty")
        else:
            self.top = self.top.next
            self.length -=1
            if self.length == 0:
                self.bottom = None

    def peek(self):
        if self.length == 0:
            return None
        return self.top
                

    def display(self):
        temp = self.top
        while temp is not None:
            print(str(temp.data))
            temp = temp.next



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
print(str(myStack.peek().data))
