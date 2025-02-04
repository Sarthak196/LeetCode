class Solution:
    def hasCycle(self, head):
        slow, fast = head, head # Hare and tortoise algorithm
        while fast and fast.next: # check if fast and fast.next are not None
            slow = slow.next # move slow by one
            fast = fast.next.next # move fast by two
            if fast == slow: # eventually fast will catch up to slow if there is a cycle
                return True
        return False
