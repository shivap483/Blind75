from typing import Optional

import ListNode


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or not head.next:
            return None
        dummy = ListNode(0)
        dummy.next = head
        first = head
        for i in range(n):
            first = first.next
        last = dummy

        while first:
            first = first.next
            last = last.next
        last.next = last.next.next
        return dummy.next
