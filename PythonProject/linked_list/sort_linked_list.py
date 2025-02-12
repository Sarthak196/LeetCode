class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def mergeSort(self, head):
        if not head or not head.next:
            return head

        middle = self.getMiddle(head)
        nextToMiddle = middle.next
        middle.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)

        sortedList = self.sortedMerge(left, right)
        return sortedList

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortedMerge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)

        return result

    def sort(self):
        self.head = self.mergeSort(self.head)

    def traverse(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

# Example usage:
sll = SinglyLinkedList()
sll.insertAtEnd(3)
sll.insertAtEnd(1)
sll.insertAtEnd(4)
sll.insertAtEnd(2)
print("Original list:", sll.traverse())  # Output: [3, 1, 4, 2]
sll.sort()
print("Sorted list:", sll.traverse())    # Output: [1, 2, 3, 4]