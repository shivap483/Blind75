# This is a sample Python script.
import datetime
import time

import RemoveNthNodeFromEnd
from ListNode import ListNode
from TreeNode import TreeNode

# def makeTree(arr, i=0):
#     if i >= len(arr):
#         return None
#     node = TreeNode(arr[i])
#     left = makeTree(arr, i + 1)
#     right = makeTree(arr, i + 2)
#     node.left = left
#     node.right = right
#     return node


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # lists = [[1,4,5],[1,3,4],[2,6]]
    input = [30130506]
    # for list in lists:
    #     input.append(ListNode.getLinkedList(list))
    t = "ABCCED"
    solution = file.Solution()
    start = time.time()
    sol = []
    for case in input:
        ans = solution.reverseBits(case)
        sol.append(ans)
    end = time.time()
    print(sol)
    print(end - start)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
