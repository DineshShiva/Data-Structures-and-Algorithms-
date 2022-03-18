class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

    def set_data(self,data):
        self.data = data

    def set_next(self,next_node):
        self.next = next_node

    def set_previous(self,previous_node):
        self.previous = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            if temp.get_previous() is not None and temp.get_next() is not None:
                print("data - " +str(temp.get_data())+ " , previous data - " + str((temp.get_previous()).get_data()) + " and next data- " + str(temp.get_next().get_data()))
            elif temp.get_previous() is not None:
                print("data - " +str(temp.get_data())+ " and  previous data - " + str((temp.get_previous()).get_data()))
            else:
                print("data - " +str(temp.get_data())+ " and next data- " + str(temp.get_next().get_data()))
                
            temp = temp.get_next()

    def __str__(self):
        temp = self.head
        dataList = []
        while temp is not None:
            dataList.append(str(temp.get_data()))
            temp = temp.get_next()
        print("Double Linked list is " + " ".join(dataList))




myList = DoubleLinkedList()

myList.add(10)
myList.add(20)
myList.add(30)
myList.add(40)
myList.add(50)

myList.prepend(33)

myList.display()















        












        
        
