"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from Node import Node


class Solution:
    def cloneGraph(self, node):
        visited = {}

        def clone(node):
            if not node:
                return None
            if node in visited:
                return visited[node]

            new_node = Node(node.val)
            visited[node] = new_node
            for neighbor in node.neighbors:
                new_node.neightbors.append(clone(neighbor))
            return new_node

        return clone(node)
