"""
https://leetcode.com/problems/bus-routes/

#2024 #favorite #bfs #revisit
"""

class Solution:
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        toRoutes = defaultdict(lambda: [])
        visitedNodes, visitedRoutes = set(), set()
        queue = [(source, 0)]

        for routeIdx, route in enumerate(routes):
            for node in route:
                toRoutes[node].append(routeIdx)

        # Very weird BFS, elects to visit entire route before jumping to a different one
        # The number of routes taken is basically the BFS dist
        # BFS on routes instead of BFS on nodes
        for node, routesCnt in queue:
            if node == target:
                return routesCnt

            for routeIdx in toRoutes[node]:
                if routeIdx in visitedRoutes:
                    continue

                route = routes[routeIdx]

                for child in route:
                    if child not in visitedNodes:
                        queue.append((child, routesCnt + 1))
                        visitedNodes.add(child)

                visitedRoutes.add(routeIdx)

        return -1
