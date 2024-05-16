"""
Done as a mock with Vishnu. He pointed out I have trouble articulating what I get stuck on.

Troubles that I had:
Deciding between adding dummy node(s) or not
Defining the different cases for remove()
Traversing the list in getValues()

https://neetcode.io/problems/singlyLinkedList

#2024
"""

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        currIndex = 0
        currNode = self.head

        while currIndex < index:
            currNode = currNode.child
            currIndex += 1

        return currNode.value

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            tmp = self.head
            self.head = Node(val)
            self.head.child = tmp

        self.length += 1

    def insertTail(self, val: int) -> None:
        if not self.tail:
            self.head = Node(val)
            self.tail = self.head
        else:
            tmp = self.tail
            self.tail = Node(val)
            tmp.child = self.tail

        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        elif index == 0:
            self.head = self.head.child
        else:
            currIndex = 0
            currNode = self.head
            while currIndex < index - 1:
                currNode = currNode.child
                currIndex += 1

            targetNode = currNode.child
            currNode.child = targetNode.child

            if index == self.length - 1:
                self.tail = currNode
        
        self.length -= 1

        return True

    def getValues(self) -> List[int]:
        result = []
        currNode = self.head

        while currNode:
            result.append(currNode.value)
            currNode = currNode.child

        return result
        

class Node:
    def __init__(self, value):
        self.value = value
        self.child = None
