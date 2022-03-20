class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree(BST)
class Tree:

    def __init__(self):
        self.root = None

    def insert(self,value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        else:
            currentNode = self.root
            while(currentNode.left != newNode) and (currentNode.right != newNode):
                if currentNode.value > newNode.value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    currentNode = currentNode.right

    def lookup(self,value):
        if self.root is None:
            print("Tree is empty")
        else:
            currentNode = self.root
            while currentNode is not None:
                if currentNode.value < value:
                    currentNode = currentNode.right
                elif currentNode.value > value:
                    currentNode = currentNode.left
                elif currentNode.value == value:
                    return currentNode
            return False

    def search(self,value):
        if self.root is None:
            print("Tree is empty")
        else:
          if self.traverse(self.root,value):
              print("Found")
          else:
              print("Not Found")


    def traverse(self,node,value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif node.value > value:
            
           return self.traverse(node.left,value)
        else:
            return self.traverse(node.right,value)
        
                    
                

    def display(self,node):
        tree = {'value':node.value}
        if node.left is not None:
            tree['left'] =self.display(node.left)
        else:
            tree['left'] =  None
        if node.right is not None:
            tree['right'] = self.display(node.right)
        else:
            tree['right'] =  None
        return tree
    


myTree = Tree()

myTree.insert(9)
myTree.insert(4)
myTree.insert(6)

myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

print(str(myTree.display(myTree.root)))

myTree.search(1)

lookup = myTree.lookup(6)
if lookup is not False:
   print(myTree.display(lookup))
else:
    print("lookup not found value node")
       
