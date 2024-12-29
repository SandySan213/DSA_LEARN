"""
binary search tree is 
1. left subtree value of a node is less than or equal to its parent node's value.
2. right subtree of a node is greater than its parent node's value

why: 
    because it perform fasteer then binar tree when inserting and deleting nodes.

common operations:
    creation of tree
    insertiion of node
    deletion of node
    search for a value
    traverse all nodes
    deletion of tree
"""

from QueueLinkedList import Queue as q, Node
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild: BSTNode | None = None
        self.rightChild: BSTNode | None = None

# insert a node
def insertNode(rootNode: BSTNode, nodeValue: str):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,  nodeValue)

    return f"the node: {nodeValue} has been successfully inserted"

# traverse in BST
# DEPTH FIRST SEARCH ( DFS )
    """
        1. pre-order
        2. in-order
        3. post-order
    """

# BREADTH FIRST SEARCH (BFS)
    """
        1. level order
    """

def preOrderTraversal(rootNode: BSTNode): # O(n) DFS
    """Rootnode --> leftSubTree --> rightSubTree"""
    if not rootNode: # O(1)
        return
    print(rootNode.data) # O(1)
    preOrderTraversal(rootNode=rootNode.leftChild) # O(n/2)
    preOrderTraversal(rootNode=rootNode.rightChild) # O(n/2)

def inOrderTraversal(rootNode: BSTNode): # O(n) DFS
    """ leftSubTree --> rootnode --> rightSubTree"""
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild) # O(n/2)
    print(rootNode.data) # O(1)
    inOrderTraversal(rootNode.rightChild) # O(n/2)
     

def postOrderTraversal(rootNode: BSTNode): # O(n) DFS
    """leftSubTree --> rightSubTree --> rootNode"""
    if not rootNode: # O(1)
        return
    
    postOrderTraversal(rootNode.leftChild) # O(n/2)
    postOrderTraversal(rootNode.rightChild) # O(n/2)
    print(rootNode.data)  # O(1)

def levelOrderTraversal(rootNode: BSTNode): # BFS 
    if not rootNode: # O(1)
        return
    else:
        customeQueue = q() # O(1) 
        customeQueue.enqueue(rootNode) # O(1)
        while not (customeQueue.isEmpty()): # O(n)
            queue: Node = customeQueue.dequeue() # O(1)
            root: BSTNode = queue.value
            print(queue.data)
            
            if (root.leftChild is not None): # O(1)
                customeQueue.enqueue(root.leftChild)
            
            if (root.rightChild is not None): # O(1)
                customeQueue.enqueue(root.rightChild)


def searchBinaryTree(rootNode: BSTNode, nodeValue: int  ): # same as `level order` time & space complexity
    """search a node value exists in binary search tree
    """
    
    if rootNode.data == nodeValue:
        return True
    elif nodeValue < rootNode.data:
        if rootNode.leftChild:
            if rootNode.leftChild.data == nodeValue:
                return True
            else:
                return searchBinaryTree(rootNode.leftChild, nodeValue)

    else:
        if rootNode.rightChild:
            if rootNode.rightChild.data == nodeValue:
                return True
            else:
                return searchBinaryTree(rootNode.rightChild, nodeValue)
            
def minValueNode(bstNode: BSTNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild

    return current
        
def deleteNode(rootNode: BSTNode, nodeValue: int):
    if rootNode is None:
        return rootNode

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)

    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)


    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode

if __name__=='__main__':

    #creation of tree
    newBST = BSTNode(None)

    print(insertNode(newBST, 70))
    print(insertNode(newBST, 60))
    print(insertNode(newBST, 50))
    print(insertNode(newBST, 20))
    print(insertNode(newBST, 90))
    print(insertNode(newBST, 10))

    print("parent node is: ",newBST.data)
    print("left node is: ",newBST.leftChild.data)
    print("right node is: ",newBST.rightChild.data)

    # preOrderTraversal(rootNode=newBST)

    # inOrderTraversal(rootNode=newBST)

    # postOrderTraversal(rootNode=newBST)

    # levelOrderTraversal(rootNode=newBST)

    print(searchBinaryTree(rootNode=newBST, nodeValue=5))
