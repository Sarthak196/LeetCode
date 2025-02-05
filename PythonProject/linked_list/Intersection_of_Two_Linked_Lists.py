# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        curr1, curr2 = headA, headB
        while curr1!= curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA
        return curr1

# this is called 3+2=5 and 2+3=5 method. Here the curr1 first traverses it own path before jumping to
# the path of list2 and vice-versa. This is done so that both the linked list come out to be of same
# length. Keep comparing the address of both the node in while loop.