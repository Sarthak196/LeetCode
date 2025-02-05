# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        curr1, curr2 = l1, l2
        dummy = dummyNode = ListNode()
        carry = 0
        while curr1 or curr2 or carry!=0: #if carry is not zero, then we need to add it to the new node
            digit1 = curr1.val if curr1 else 0
            digit2 = curr2.val if curr2 else 0
            sum = digit1 + digit2 + carry
            digit = sum%10 # get the digit which is the last digit of the sum
            carry = sum//10 # get the carry which is the first digit of the sum
            newNode = ListNode(digit)
            dummy.next = newNode # add the new node to the dummy linked list
            dummy = dummy.next
            curr1 = curr1.next if curr1 else None # move the pointers to the next node if they are not None
            curr2 = curr2.next if curr2 else None
        return dummyNode.next