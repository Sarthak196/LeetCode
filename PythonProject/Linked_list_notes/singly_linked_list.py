class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
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
        curr.next = newNode

    def deleteAtBeginning(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next

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
        prev = None
        for i in range(index):
            if curr is None:
                print("Index out of range")
                return
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def size(self):
        if self.head is None:
            return 0
        curr = self.head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next



s = SinglyLinkedList()
s.insertAtBeginning(1)
s.insertAtBeginning(2)
s.insertAtBeginning(3)
s.insertAtBeginning(4)
s.insertAtEnd(5)
s.insertAtIndex(6, 2)
print(f"Size of linked list: {s.size()}")
s.printLL()
s.deleteAtBeginning()
s.deleteAtEnd()
print("After deletion")
s.printLL()
s.deleteAtIndex(2)
print("After deletion")
s.printLL()

