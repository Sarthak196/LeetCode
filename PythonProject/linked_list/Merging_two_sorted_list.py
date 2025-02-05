# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        curr = dummy = ListNode() #create a dummy node with None value and assign it to curr
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next # curr.next is decided based on which val is smaller between list1 and list2
        if list1:
            curr.next = list1
        else:
            curr.next = list2 # if any of the list reaches tail before another then the curr.next is the longer list
        return dummy.next # return dummy.next as current dummy's head has None value