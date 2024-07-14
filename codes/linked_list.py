class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.head.next = self.tails
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def __iter__(self):
        tmp_node = self.head
        while tmp_node is not None:
            yield tmp_node.value
            tmp_node = tmp_node.next

    def __str__(self) -> str:
        lists = [str(x) for x in self]
        return f"[{','.join(lists)}]"
    
    def __getitem__(self, index):
        if self.head is None or index > self.length - 1:
            raise IndexError('linked list index is out of range!')
        tmp_node = self.head
        for _ in range(0,index):
            tmp_node = tmp_node.next
        
        return tmp_node.value


