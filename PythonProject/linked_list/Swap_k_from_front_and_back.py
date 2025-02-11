# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def swapNodes(self, head, k):
        left, right = head, head
        for _ in range(1,k): # move the left pointer to the kth position
            left = left.next
        window = left # as right is head and left is at kth position, there is a window created
        while window.next: # slide the window along with right to get the kth pos from end
            right = right.next
            window = window.next
        left.val, right.val = right.val, left.val # swap the values
        return head