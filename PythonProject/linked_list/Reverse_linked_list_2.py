# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left ==  right:
            return head
        prev = dummy = ListNode(-1, head) #create a dummy node to handle the edge case of left = 1
        for i in range(left-1):
            prev = prev.next #move the prev pointer to the node before the left node
        curr = prev.next #curr is the left node
        for i in range(right-left):
            temp = curr.next #temp is the node to be reversed
            curr.next = temp.next #move the next pointer of the left node to the node after the node to be reversed
            temp.next = prev.next #move the next pointer of the node to be reversed to the node after the left node
            prev.next = temp #move the next pointer of the prev node to the node to be reversed
        return dummy.next

