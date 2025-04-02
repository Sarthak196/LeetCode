from PythonProject.linked_list.Reverse_linked_list import linkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head or not head.next: # if the list is empty or has only one node, return the head
            return head

        dummyNode = ListNode(0) # create a dummy node to simplify the swapping process
        prev, curr = dummyNode, head # prev is the previous node or dummy node, curr is the current node or head

        while curr and curr.next:
            npn = curr.next.next # npn is the next node after the current pair
            sec = curr.next # sec is the second node in the current pair

            sec.next = curr # point the second node to the first node
            curr.next = npn # point the first node to the next node after the current pair
            prev.next = sec # point the previous node to the second node in the current pair

            prev = curr # move the previous pointer to the first node in the current pair
            curr = npn # move the current pointer to the next node after the current pair

        return dummyNode.next # return the new head of the swapped linked list
