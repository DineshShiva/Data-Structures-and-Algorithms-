class Node:
    def __init__(self,data):

        self.data = data
        self.next = None

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self,next_node):
        self.next = next_node

    def get_next(self):
        return self.next

class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def prepend(self,data):
      new_node = Node(data)
      if self.head is None:
          self.head = self.tail = new_node
      else:
          new_node.set_next(self.head)
          self.head = new_node


    def insertIndex(self,index,data):
        if index == 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            leadNode = self.traverseToIndex(index-1)
            if leadNode is not None:
               new_node.set_next(leadNode.get_next())
               leadNode.set_next(new_node)
               if new_node.get_next() is None:
                  self.tail = new_node
            else:
                self.add(data)

    def removeIndex(self,index):
        node = self.traverseToIndex(index)
        if node is not None:
            if index == 0:
                self.head = node.get_next()
            else:
                temp = self.head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.tail:
                            self.tail =temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
           print("List index is out of range")

                    
        


    def traverseToIndex(self,index):
        counter=0
        temp = self.head
        while temp is not None:
            if counter == index:
                return temp
            counter+=1
            temp = temp.get_next()
        return None
        
                    


    def insert(self,data,data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.head)
            self.head = new_node
            if new_node.get_next() is None:
                self.tail = new_node
        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.tail = new_node
            else:
                print("sorry there is no data exists in list to add new data")



    def delete(self,data):
        node = self.find_node(data)
        if node is not None:
            if node == self.head:
                if node == self.tail:
                    self.tail = None
                self.head = node.get_next()
            else:
                temp = self.head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.tail:
                            self.tail = temp
                        node.set_next(None)
                        break
                    temp =temp.get_next()
        else:
            print(data," isn't present in LinkedList")


    def find_node(self,data):
        temp = self.head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

#Otherwise, we create two nodes first and second which point to the first and second nodes of the list respectively
#Then we update the tail of the list to point to the head as after reversing the present head will become the last node
#Then we run a loop until second becmes None
#Inside the loop we create a temporary node which points to the 'next' of the second node
#Then we update the 'next' of the second node to point to the first node so that the link is now reversed (2nd node points to 1st node instead of 3rd).
#And then we will update the first and second nodes to be equal to the second and temporary nodes respectively.
#What this does is, in the next iteration, 'second' will point to the 3rd node and 'first' to the 2nd
#And the 'second.next = first' statement will make the 3rd node point to the 2nd node instead of the 4th.
#And this will go on till 'second' becomes None and by then all the links will be reversed.
#Finally, we will update the 'next' of the head(which is still the original head) point to None as it is effectively the last node
#And then we will update the head to be equal to 'first', which by now points to the last node of the original list, and return the now reversed linked list
#Time complexity pretty clearly will be O(n)
    def reverse(self):
        if self.head.get_next() is None:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.get_next()
        while second is not None:
            temp = second.get_next()
            second.set_next(first)
            first = second
            second = temp
        self.head.set_next(None)
        self.head = first
        return self


    
            
    def display(self):
        temp = self.head
        while temp is not None:
             print(temp.get_data())
             temp = temp.get_next()
             
    def __str__(self):
        temp = self.head
        dataList = []
        while temp is not None:
            dataList.append(str(temp.get_data()))
            temp = temp.get_next()
        print("Linked List : " + " ".join(dataList))


myList = LinkedList()

myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)
myList.add(6)

myList.__str__()

myList.reverse()

myList.__str__()

myList.insert(4.5,4)

myList.delete(3)

myList.prepend(20)

myList.insertIndex(2,300)

myList.removeIndex(4)

myList.display()













        
