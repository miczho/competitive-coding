"""
Keep a doubly linked list of buckets holding keys with the same value.
Each bucket can be accessed in O(1) time via hashing.
If a bucket goes from empty to filled, insert into list.
If a bucket goes from filled to empty, remove from list.

https://leetcode.com/problems/all-oone-data-structure

#favorite #linkedList #2024
"""

from collections import defaultdict

class Bucket:
    def __init__(self, key=None):
        self.keys = set() if key == None else set([key])
        self.prev = None
        self.next = None

    def __len__(self):
        return len(self.keys)

    def insertBefore(self, bucket):
        if self.prev != None:
            self.prev.next = bucket
            bucket.prev = self.prev
        self.prev = bucket
        bucket.next = self

    def insertAfter(self, bucket):
        if self.next != None:
            self.next.prev = bucket
            bucket.next = self.next
        self.next = bucket
        bucket.prev = self

    def delete(self):
        if self.prev != None:
            self.prev.next = self.next
        if self.next != None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

    def getKey(self):
        return next(iter(self.keys), "")


class SentinalBucket(Bucket):
    def __len__(self):
        return 1


class AllOne(object):
    def __init__(self):
        self.map = defaultdict(lambda: 0)
        self.bucket = defaultdict(lambda: Bucket())
        self.head = SentinalBucket()
        self.tail = SentinalBucket()

        self.bucket[0] = self.head
        self.head.insertAfter(self.tail)

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        currVal = self.map[key]
        nextVal = currVal + 1
        currBucket = self.bucket[currVal]
        nextBucket = self.bucket[nextVal]

        self.map[key] = nextVal

        currBucket.keys.discard(key)
        if len(nextBucket) == 0:
            currBucket.insertAfter(nextBucket)
        if len(currBucket) == 0:
            currBucket.delete()
        nextBucket.keys.add(key)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        currVal = self.map[key]
        nextVal = currVal - 1
        currBucket = self.bucket[currVal]
        nextBucket = self.bucket[nextVal]

        self.map[key] = nextVal

        currBucket.keys.discard(key)
        if len(nextBucket) == 0:
            currBucket.insertBefore(nextBucket)
        if len(currBucket) == 0:
            currBucket.delete()
        if nextVal != 0:
            nextBucket.keys.add(key)

    def getMaxKey(self):
        """
        :rtype: str
        """
        return self.tail.prev.getKey()

    def getMinKey(self):
        """
        :rtype: str
        """
        return self.head.next.getKey()



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
