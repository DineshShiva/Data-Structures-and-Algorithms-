class Node:

    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev = None

    def set_data(self):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self,next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def set_prev(self,prev_node):
        self.prev = prev_node

    def get_prev(self):
        return self.prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    def traverseToIndex(self,index):
        counter = 0
        temp = self.head
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.get_next()
            counter+=1
        return None

    def insertAtIndex(self,index,data):
        if index == 0:
            self.prepend(data)
        else:
            leadNode = self.traverseToIndex(index-1)
            if leadNode is not None:
                new_node = Node(data)
                follow_node = leadNode.get_next()
                leadNode.set_next(new_node)
                new_node.set_prev(leadNode)
                new_node.set_next(follow_node)
                follow_node.set_prev(new_node)
                if new_node.get_next() is None:
                    self.tail = new_node
            else:
                self.append(data)

    def deleteAtIndex(self,index):
        node = self.traverseToIndex(index)
        if node is not None:
           if index == 0:
               follow_node = self.head.get_next()
               follow_node.set_prev(None)
               self.head = follow_node
           else:
               lead_node = node.get_prev()
               follow_node = node.get_next()
               if node == self.tail:
                   lead_node.set_next(None)
                   self.tail = lead_node
               else:
                 lead_node.set_next(follow_node)
                 follow_node.set_prev(lead_node)
        else:
            print("List index is out of index")

    def findDataNode(self,data):
        temp = self.head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def insertAfterData(self,data,data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
            if new_node.get_next() is None:
                self.tail = new_node

        else:
            lead_node = self.findDataNode(data_before)
            if lead_node is not None:
                if lead_node == self.tail:
                    lead_node.set_next(new_node)
                    new_node.set_prev(lead_node)
                    self.tail = new_node
                else:
                    follow_node = lead_node.get_next()
                    lead_node.set_next(new_node)
                    new_node.set_prev(lead_node)
                    new_node.set_next(follow_node)
                    follow_node.set_prev(new_node)
            else:
                print("data isn't present in List")

    def deleteData(self,data):
        node = self.findDataNode(data)
        if node is not None:
            lead_node = node.get_prev()
            follow_node = node.get_next()
            if node == self.head:      
                self.head = follow_node
                follow_node.set_prev(None)
            elif node == self.tail:   
                self.tail = lead_node
                lead_node.set_next(None)
            else:
                lead_node.set_next(follow_node)
                follow_node.set_prev(lead_node)
        else:
            print("data isn't present in list")

    

    def display(self):
        temp = self.head
        while temp is not None:
            if temp.get_prev() is not None and temp.get_next() is not None:
               print("data - " +str(temp.get_data()) + " , previous data - " + str(temp.get_prev().get_data())  + " and next data - " + str(temp.get_next().get_data()))
            elif temp.get_prev() is None:
               print("data - " +str(temp.get_data()) + " , previous data - None and next data - " + str(temp.get_next().get_data()))
            else:
               print("data - " +str(temp.get_data())+ " , previous data - "+ str(temp.get_prev().get_data()) +" and next data - None")
            temp = temp.get_next()

    def __str__(self):
        temp = self.head
        dataList = []
        while temp is not None:
            dataList.append(str(temp.get_data()))
            temp = temp.get_next()
        return dataList




myList = DoublyLinkedList()

myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)

myList.display()

myList.prepend(200)
myList.prepend(400)

print("\n")
myList.display()

myList.insertAtIndex(3,33)

print("\n")
myList.display()

myList.deleteAtIndex(5)

print("\n")
myList.display()

myList.insertAfterData(28,33)

print("\n")
myList.display()

myList.deleteData(10)

print("\n")
myList.display()





















        





                
            

       














        
            
































        
