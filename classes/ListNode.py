class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getLinkedList(arr):
        head = ListNode(0)
        temp = head
        for val in arr:
            node = ListNode(val)
            temp.next = node
            temp = temp.next
        return head.next
