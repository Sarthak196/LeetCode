def reorderList(head) :
    slow, fast, fir_start = head, head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next #finding the middle element
    mid_start = slow.next # 2nd half will be the head
    prev = slow.next = None # end the 1st half by pointing it's last element's next to none
    while mid_start:
        post = mid_start.next
        mid_start.next = prev
        prev = mid_start
        mid_start = post # reverse the 2nd half
    sec_start = prev
    while sec_start: # always 2nd half will be shorter
        fir_post = fir_start.next
        sec_post = sec_start.next
        fir_start.next = sec_start
        sec_start.next = fir_post
        fir_start = fir_post
        sec_start = sec_post # re-ordering

# linked_list: 0->1->2->3->4->5->6
# return 1, n-1, 2, n-2, 3, n-3...
# 0->6->1->5->2->4->3