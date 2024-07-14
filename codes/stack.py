class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self) -> str:
        return str(self.value)


class LinkedList: # for stack tail is not needed
    """_summary_
    """
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
"""stack method are
push
pop
peek
isEmpty
delete 
"""

class Stack:
    """_summary_
    """

    def __init__(self):
        self.linkedList = LinkedList()
        
    def __str__(self) -> str:
        values = [str(x) for x in self.linkedList]
        return f"[{','.join(values)}]"
    
    def isEmpty(self):
        return self.linkedList.head == None
    
    def push(self, value):
        """_summary_

        Args:
            value (str): value to be added in stack
        """
        new_node = Node(value)
        new_node.next = self.linkedList.head
        self.linkedList.head = new_node

    def pop(self):
        if self.isEmpty():
            return "no elements are available in stack!."
        nodeValue = self.linkedList.head.value
        
    def peek(self):
        """_summary_

        Returns:
            str | int: return last inserted value in the linked list
        """
        if self.isEmpty():
            return "stack is empty"
        return self.linkedList.head.value
    
    def delete(self):
        self.linkedList.head = None
        return 'deleted'
