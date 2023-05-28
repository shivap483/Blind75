class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getLinkedList(arr):
        head = None
        temp = head
        for val in arr:
            node = ListNode(val)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = temp.next
        return head