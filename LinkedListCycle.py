# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Notes:
# sol 1: use hashing to store nodes ans it's indexes. if while trversing, we encounter null, then there is cycle, if we encounter a visited node, then there is a cycle
# sol 2: use fast and slow pointers if the pointer meet at any point, then there is cycle. if any of the pointer is null, then there is no cycle.


class Solution:
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
