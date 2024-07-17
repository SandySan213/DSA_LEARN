# from queue import Queue as q
from QueueLinkedList import Queue as q, Node

class Treenode:
    def __init__(self, data: str):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBT = Treenode(data='Drinks')
leftChild = Treenode(data="Hot")
rightChild = Treenode(data="Cold")
lLeftchild = Treenode(data='tea')
lRightChild = Treenode(data='coffee')
leftChild.leftChild = lLeftchild
leftChild.rightChild = lRightChild
rLeftchild = Treenode(data='fanta')
rRightChild = Treenode(data='pepsi')
rightChild.leftChild = rLeftchild
rightChild.rightChild = rRightChild
newBT.leftChild = leftChild
newBT.rightChild = rightChild
 
# O(n) ----> Linear time complexity. and O(n) space complexity because we are using recursive.
 
# DEPTH FIRST SEARCH ( DFS)  

# BREADTH FIRST SeARCH (BFS)

def preOrderTraversal(rootNode: Treenode): # O(n) DFS
    """Rootnode --> leftSubTree --> rightSubTree"""
    if not rootNode: # O(1)
        return
    print(rootNode.data) # O(1)
    preOrderTraversal(rootNode=rootNode.leftChild) # O(n/2)
    preOrderTraversal(rootNode=rootNode.rightChild) # O(n/2)


# preOrderTraversal(rootNode=newBT)


def inOrderTraversal(rootNode: Treenode): # O(n) DFS
    """ leftSubTree --> rootnode --> rightSubTree"""
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild) # O(n/2)
    print(rootNode.data) # O(1)
    inOrderTraversal(rootNode.rightChild) # O(n/2)
     
# inOrderTraversal(rootNode=newBT) 

def postOrderTraversal(rootNode: Treenode): # O(n) DFS
    """leftSubTree --> rightSubTree --> rootNode"""
    if not rootNode: # O(1)
        return
    
    postOrderTraversal(rootNode.leftChild) # O(n/2)
    postOrderTraversal(rootNode.rightChild) # O(n/2)
    print(rootNode.data)  # O(1)

# postOrderTraversal(rootNode=newBT)

def levelOrderTraversal(rootNode: Treenode): # BFS 
    if not rootNode: # O(1)
        return
    else:
        customeQueue = q() # O(1) 
        customeQueue.enqueue(rootNode) # O(1)
        while not (customeQueue.isEmpty()): # O(n)
            root: Node = customeQueue.dequeue() # O(1)
            print(root.value.data)
            
            if (root.value.leftChild is not None): # O(1)
                customeQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None): # O(1)
                customeQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(rootNode=newBT)

def searchBinaryTree(rootNode: Treenode, nodeValue: str | int | float ): # same as `level order` time & space complexity
    """search a node value exists in binary tree
    """
    if not rootNode:
        return "The Binary tree is not exist"
    else:
        customQueue = q()
        customQueue.enqueue(rootNode)
         
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return True
            
            if (root.value.leftChild is not None): # O(1)
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None): # O(1)
                customQueue.enqueue(root.value.rightChild)
        return f"root node with value `{nodeValue}` is not exist"
                
# print(searchBinaryTree(rootNode=newBT, nodeValue='fanta'))

def insertBinaryTree(rootNode, newNode): # same as `level order` time & space complexity
    """ Insert a new node in the binary tree """
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = q()
        
        root: Treenode = customQueue.enqueue(rootNode)
        
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
                   
            if (root.value.leftChild is not None): # O(1)
                customQueue.enqueue(root.value.leftChild)
            
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            
            if (root.value.rightChild is not None): # O(1)
                customQueue.enqueue(root.value.rightChild)
            
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"
            
        return "cannot insert a new Node!."

new_node = Treenode(data='red bull')

# print(insertBinaryTree(rootNode=newBT, newNode=new_node))

# levelOrderTraversal(rootNode=newBT)

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = q()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):

            root = customQueue.dequeue()            
            if (root.value.leftChild is not None): # O(1)
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None): # O(1)
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

# deppest_node = getDeepestNode(rootNode=newBT)
# print(deppest_node.data)


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = q()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "BT does not exist"
    else:
        customQueue = q()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been succesfully deleted"
            
            if (root.value.leftChild is not None): # O(1)
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None): # O(1)
                customQueue.enqueue(root.value.rightChild)
            

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BT is deleted!"

deleteBT(newBT)
levelOrderTraversal(newBT)

# levelOrderTraversal(newBT)
# print('*' * 100)
# deepNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, deepNode)
# deleteNodeBT(newBT, 'coffee')
# levelOrderTraversal(newBT)
