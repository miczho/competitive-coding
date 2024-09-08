"""
Time Complexity:
O(V + E)

Space Complexity:
O(V + E)

https://neetcode.io/problems/course-schedule-ii
https://leetcode.com/problems/course-schedule-ii

#2024 #neetcode150 #topSort
"""

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        children = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for v, u in prerequisites:
            children[u].append(v)
            inDegree[v] += 1

        queue = [i for i in range(numCourses) if inDegree[i] == 0]

        for course in queue:
            for child in children[course]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)

        return queue if len(queue) == numCourses else []
