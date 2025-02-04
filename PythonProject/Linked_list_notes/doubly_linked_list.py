class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBeginning(data)
            return
        newNode = Node(data)
        curr = self.head
        for i in range(index - 1):
            if curr is None:
                print("Index out of range")
                return
            curr = curr.next
        newNode.next = curr.next
        curr.next.prev = newNode
        curr.next = newNode
        newNode.prev = curr

    def deleteAtBeginning(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next
        self.head.prev = None

    def deleteAtEnd(self):
        if self.head is None:
            print("list is empty")
            return
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None

    def deleteAtIndex(self, index):
        if self.head is None:
            print("list is empty")
            return
        if index == 0:
            self.deleteAtBeginning()
            return
        curr = self.head
        for i in range(index):
            if curr is None:
                print("Index out of range")
                return
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()