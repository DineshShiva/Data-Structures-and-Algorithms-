class Node:

    def __init__(self,data):
        self.data =  data
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1

    def dequeue(self):
        if self.length == 0:
            print("Queue is empty")
            return
        elif self.first == self.last:
            self.last = None
        # can return this  for later use even deleting from queue have access to this node
        holdingPointer  = self.first 
        self.first = self.first.next
        self.length -=1
            

    def peek(self):
        return self.first

    def display(self):
        temp = self.first
        while temp is not None:
            print(str(temp.data))
            temp =temp.next

    def __str__(self):
        temp = self.first
        dataQueue = []
        while temp is not None:
            dataQueue.append(str(temp.data))
            temp =temp.next
        print(dataQueue)



myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)

myQueue.__str__()

myQueue.dequeue()
myQueue.dequeue()

print("/n")
myQueue.__str__()

myQueue.peek()

print("/n")
myQueue.__str__()
        
