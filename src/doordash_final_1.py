"""
===== Problem: Compare N-ary Trees =====

You are given an n-ary tree 'tree1'. Each node in the tree has the following attributes:
    1. key - A unique identifier for the node that cannot be changed.
    2. value - An integer value associated with the node.
    3. children - A list of child nodes.

A modified version of this tree, 'tree2', has been created by applying a series of changes to 'tree1'. 
These changes can include:
    1. Adding a Node - A new node is added to 'tree2' that did not exist in 'tree1'.
    2. Removing a Node - A node that existed in 'tree1' is removed in 'tree2' (can only be performed if the node is presently a leaf).
    3. Changing a Node's Value - The value of a node in 'tree1' is changed in 'tree2'.

Your task is to write a function 'countDifferences(tree1: Node, tree2: Node) -> int'
that counts the number of modifications made to transform 'tree1' into 'tree2'.

===== Input =====

'tree1' and 'tree2' are the root nodes of the original and modified n-ary trees, respectively.

Each tree node has:
    1. A unique key (string).
    2. A value (integer).
    3. A list of children (list of nodes).

===== Output =====

An integer representing the total number of modifications made to 'tree1' to produce 'tree2'.

===== Examples =====

Input:
    A(1)
    ├── B(2)
    └── C(3)

    A(1)
    ├── B(4)
    └── D(5)

Output: 3

================================

Input:
    A(1)
    ├── B(2)
    ├── C(3)
    └── D (4)

    A(1)
    ├── D(4)
    ├── B(2)
    └── C(3)

Output: 0

================================

Input:
    A(1)
    ├── B(2)
    │   ├── D(4)
    │   └── E(5)
    └── C(3)
        └── F(6)

    A (1)
    ├── B(2)
    │   ├── D(4)
    │   ├── E(555)
    │   └── G(7)
    └── H(99)
        └── F(6)

Output: 6

Explanation:
    1. Change value E(5) -> E(555)
    2. Add G(7)
    3. Remove F(6)
    4. Remove C(3)
    5. Add H(99)
    6. Add F(6)





Time Complexity:
O(N + M)

Space Complexity:
O(N + M)

Where N = # of nodes in 'tree1' and M = # of nodes in 'tree2'

#interview #favorite #dfs #bfs #2024
"""

from typing import List
from collections import defaultdict

class Node:
    def __init__(self, key: str, value: int, children: List['Node'] = []):
        self.key = key
        self.value = value
        self.children = children

def countDifferences(tree1: Node, tree2: Node) -> int:
    def dfs(node1, node2):
        children1, children2 = defaultdict(lambda: None), defaultdict(lambda: None)
        keys = set()
        result = 0

        for child in getattr(node1, "children", []):
            children1[child.key] = child
            keys.add(child.key)
        for child in getattr(node2, "children", []):
            children2[child.key] = child
            keys.add(child.key)

        for key in keys:
            result += dfs(children1[key], children2[key])

        if getattr(node1, "value", None) != getattr(node2, "value", None):
            result += 1

        return result

    sentinel1, sentinel2 = Node("", 0, [tree1] if tree1 else []), Node("", 0, [tree2] if tree2 else [])

    return dfs(sentinel1, sentinel2)




"""
Attempt 2: BFS solution

Time Complexity:
O(N + M)

Space Complexity:
O(N + M)

Where N = # of nodes in 'tree1' and M = # of nodes in 'tree2'
"""

# from collections import deque, defaultdict

# def countDifferences(tree1: Node, tree2: Node) -> int:
#     sentinel1, sentinel2 = Node("", 0, [tree1] if tree1 else []), Node("", 0, [tree2] if tree2 else [])
#     queue = deque([sentinel1, sentinel2])
#     result = 0
    
#     while len(queue) != 0:
#         node1, node2 = queue.popleft(), queue.popleft()
#         children1, children2 = defaultdict(lambda: None), defaultdict(lambda: None)
#         keys = set()

#         for child in getattr(node1, "children", []):
#             children1[child.key] = child
#             keys.add(child.key)
#         for child in getattr(node2, "children", []):
#             children2[child.key] = child
#             keys.add(child.key)

#         for key in keys:
#             queue.append(children1[key])
#             queue.append(children2[key])

#         if getattr(node1, "value", None) != getattr(node2, "value", None):
#             result += 1

#     return result


tree1 = Node("A", 1, [
    Node("B", 2),
    Node("C", 3)
])
tree2 = Node("A", 1, [
    Node("B", 4),
    Node("D", 5)
])
print(countDifferences(tree1, tree2))  # expected output: 3


tree1 = Node("A", 1, [
    Node("B", 2),
    Node("C", 3),
    Node("D", 4)
])
tree2 = Node("A", 1, [
    Node("D", 4),
    Node("B", 2),
    Node("C", 3)
])
print(countDifferences(tree1, tree2))  # expected output: 0


tree1 = Node("A", 1, [
    Node("B", 2, [
        Node("D", 4),
        Node("E", 5)
    ]),
    Node("C", 3, [
        Node("F", 6)
    ])
])
tree2 = Node("A", 1, [
    Node("B", 2, [
        Node("D", 4),
        Node("E", 555),
        Node("G", 7)
    ]),
    Node("H", 99, [
        Node("F", 6)
    ])
])
print(countDifferences(tree1, tree2))  # expected output: 6


tree1 = Node("A", 1, [
    Node("B", 2, [
        Node("D", 4),
        Node("E", 5)
    ]),
    Node("C", 3, [
        Node("F", 6),
        Node("G", 7)
    ])
])
tree2 = Node("A", 1, [
    Node("B", 2, [
        Node("D", 4),
        Node("E", 5),
        Node("H", 8)
    ]),
    Node("I", 99, [
        Node("F", 6),
        Node("G", 7777777777777)
    ])
])
print(countDifferences(tree1, tree2))  # expected output: 7


tree1 = None
tree2 = None
print(countDifferences(tree1, tree2))  # expected output: 0


tree1 = Node("A", 1, [
    Node("B", 2),
    Node("C", 3)
])
tree2 = Node("D", 1, [
    Node("E", 4),
    Node("F", 5)
])
print(countDifferences(tree1, tree2))  # expected output: 6


tree1 = Node("A", 1, [
    Node("B", 2),
    Node("C", 3)
])
tree2 = None
print(countDifferences(tree1, tree2))  # expected output: 3
