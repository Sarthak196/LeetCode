# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = dummyNode = ListNode(-111) # Create a dummy node
        duplicate = 111
        if head and head.next: # check if the linked list is not empty or has only one element
            left = head
            right = left.next # right is one step ahead of left
        else:
            return head
        while left:

            if right and left.val != right.val and left.val != duplicate:
                dummy.next = left # if right is not none or the current left value is not equal to right or duplicate
                                  # value
                dummy = dummy.next
            elif right is None and left.val != duplicate: # if right is none that means left is at last element, check \
                                                          # if it is not duplicate
                dummy.next = left
                dummy = dummy.next

            duplicate = left.val # update duplicate value
            left = left.next
            right = right.next if right is not None else None
        dummy.next = None
        return dummyNode.next

