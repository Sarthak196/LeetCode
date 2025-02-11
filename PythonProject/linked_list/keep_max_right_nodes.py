# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def removeNodes(self, head):
        stack = []
        curr = head
        while curr: # put all the values of linked list in a stack
            stack.append(curr)
            curr = curr.next
        minval = float("-inf")
        newhead = None
        while stack:
            node = stack.pop() # start from the last element
            if node.val >= minval: # if last element is greater than minval
                node.next = newhead # make the node as the tail
                newhead = node
                minval = node.val # change the minval
# as the nodes keep coming, keep adding them before the previous node
        return newhead