"""
#lru-cache
"""

class Node():
    def __init__(self, key, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node('head')
        self.tail = Node('tail')

        self.head.nxt = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ans = -1

        if key in self.cache:
            node = self.cache[key]

            ans = node.val
            self.removeNode(node)
            self.addNode(node)

        # self.printCache()
        return ans
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.prev.key]
                self.removeNode(self.tail.prev)
            
            node = Node(key, value)
            self.cache[key] = node
            self.addNode(node)
        else:
            node = self.cache[key]

            node.val = value
            self.removeNode(node)
            self.addNode(node)

        # self.printCache()


    def removeNode(self, node):
        p = node.prev
        n = node.nxt
        p.nxt = n
        n.prev = p


    def addNode(self, node):
        n = self.head.nxt
        n.prev = node
        self.head.nxt = node
        node.prev = self.head
        node.nxt = n


    def printCache(self):
        print('cache: { ', end='')

        node = self.head
        while node != None:
            print(f'{node.key}: {node.val}, ', end='')
            node = node.nxt

        print('}')
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)