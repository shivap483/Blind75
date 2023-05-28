# This is a sample Python script.
import datetime
import time

import WordSearch as file
from ListNode import ListNode


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # lists = [[1,4,5],[1,3,4],[2,6]]
    input = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # for list in lists:
    #     input.append(ListNode.getLinkedList(list))
    t = "ABCCED"
    solution = file.Solution()
    start = time.time()
    ans = solution.exist(input, t)
    end = time.time()
    print(ans)
    print(end - start)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
