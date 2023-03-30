class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, number):
        node = Node(number)

        if self.root is None:
            self.root = node
        else:
            currentNode = self.root

            while True:
                previousNode = currentNode
                if node.data <= currentNode.data:
                    currentNode = currentNode.left
                    if currentNode is None:
                        previousNode.left = node
                        return
                else:
                    currentNode = currentNode.right
                    if currentNode is None:
                        previousNode.right = node
                        return
                    
    def nodeSuccessor(self, nodeRemove): 
        dadSuccessor = nodeRemove
        successor = nodeRemove
        currentNode = nodeRemove.right

        while currentNode != None:
            dadSuccessor = sucessor
            successor = currentNode
            currentNode = currentNode.left

        if successor != nodeRemove.right:
            dadSuccessor.left = successor.right
            successor.right = nodeRemove.right
            
        return successor

    def remove(self, number):
        if self.root is None:
            return False 
        currentNode = self.root
        dad = self.root
        childLeft = True
        
        while currentNode.data != number:
            dad = currentNode
            if number < currentNode.data:
                currentNode = currentNode.left
                childLeft = True
            else:
                currentNode = currentNode.right
                childLeft = False
            if currentNode is None:
                return False
            
        if currentNode.left == None and currentNode.right == None:
            if currentNode == self.root:
                self.root = None
            else:
                if childLeft:
                    dad.left = None
                else:
                    dad.right = None
        
        elif currentNode.right == None:
            if currentNode == self.root:
                self.root = currentNode.left
            else:
                if childLeft:
                    dad.left = currentNode.left
                else:
                    dad.right = currentNode.left
        
        elif currentNode.left == None:
            if currentNode == self.root:
                self.root = currentNode.right
            else:
                if childLeft:
                    dad.left = currentNode.right
                else:
                    dad.right = currentNode.right
                    
        else:
            sucessor = self.nodeSuccessor(currentNode)
            
            if currentNode == self.root:
                self.root = sucessor
            else:
                if childLeft:
                    dad.left = sucessor
                else:
                    dad.right = sucessor
            sucessor.left = currentNode.left
            
        return True
    
    def inOrder(self, current):
        if current != None:
            self.inOrder(current.left)
            print(current.data,end=" ")
            self.inOrder(current.right)

    def showTree(self):
        print("Árvore binária em ordem:")
        self.inOrder(self.root)


tree = BinaryTree()
tree.insert(10) 
tree.insert(2)
tree.insert(20)
tree.insert(5)
tree.insert(32)
tree.insert(21)

tree.remove(20)

tree.showTree()