# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        left, right = head, head
        for i in range(n):
            right = right.next #create a gap of n between left and right of size n
        if not right:
            return head.next #if right is None, then remove the first element
        while right.next: #move left and right until right reaches the end
            left = left.next #and left is just before the nth element from the end
            right = right.next
        left.next = left.next.next #remove the nth element from the end
        return head

