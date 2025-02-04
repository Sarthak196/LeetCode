class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        self.head = prev

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

ll = linkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.printList()
ll.reverse()
ll.printList()