# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0: #check if linked list is empty or has just one element
            return head
        tail = head
        length = 1
        while tail.next: # get the length of the ll and keep the tail pointer at the end of ll
            tail = tail.next
            length += 1
        tail.next = head # the end of ll is again pointed to the head
        t = length - k % length # t is the value where we need to stop as the nodes after that has to be bought at the start
        for _ in range(t):
            tail = tail.next
        newHead = tail.next # new head is next value of tail
        tail.next = None # current tail's next value is set to None
        return newHead