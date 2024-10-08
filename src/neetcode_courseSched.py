"""
This BFS solution does not work because BFS by nature traverses paths level by level,
which is not conducive to cycle detection. DFS must be used.

https://neetcode.io/problems/course-schedule
https://leetcode.com/problems/course-schedule
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = set()
        children = defaultdict(lambda: [])

        for child, node in prerequisites:
            children[node].append(child)

        def bfs(start):
            queue = [start]
            localVisited = set()

            for node in queue:
                if node in localVisited:
                    return True
                
                for child in children[node]:
                    if child not in visited:
                        queue.append(child)
                
                localVisited.add(node)
            
            visited.update(localVisited)

            return False

        for node in range(numCourses):
            cycleExists = bfs(node)
            if cycleExists:
                return False

        return True





"""
Attempt 2: DFS solution

Time Complexity:
O(N + M) where N = numCourses and M = length of prerequisites

Space Complexity:
O(N + M) where N = numCourses and M = length of prerequisites

#blind75 #neetcode150 #2024
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = set()
        currPath = set()
        children = defaultdict(lambda: [])

        for child, node in prerequisites:
            children[node].append(child)

        def dfs(node):
            if node in visited:
                return False
            if node in currPath:
                return True

            currPath.add(node)

            for child in children[node]:
                cycleExists = dfs(child)
                if cycleExists:
                    return True

            currPath.remove(node)
            visited.add(node)

            return False

        for node in range(numCourses):
            cycleExists = dfs(node)
            if cycleExists:
                return False

        return True





"""
Attempt 3: BFS and topological sort
"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        children = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        queue = []

        for child, parent in prerequisites:
            children[parent].append(child)
            inDegree[child] += 1

        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)

        for course in queue:
            for child in children[course]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)

        return len(queue) == numCourses
