"""
Problem Statement:
You are given a graph representing a section of the New York City subway system. The nodes in the graph are subway stations, and the edges between them represent the time (in minutes) needed to travel from one station to another. Your task is to determine the quickest travel route from the "WTC" station to the "Bryant Park" station.

Graph Representation:
Nodes: Each node represents a subway station.
Edges: Each edge between two nodes represents the time in minutes to travel directly between those two stations.

Input:
A dictionary graph where:
The keys are strings representing station names.
The values are lists of tuples, where each tuple contains a neighboring station and the time in minutes to travel to that station.
Two strings, start and end, representing the starting station ("WTC") and the destination station ("Bryant Park").

Output:
An integer representing the minimum time required to travel from "WTC" to "Bryant Park".

Input Data:
graph = {
   "WTC": [("Chambers St", 2), ("Cortlandt St", 3)],
   "Chambers St": [("Brooklyn Bridge", 2), ("WTC", 2)],
   "Cortlandt St": [("Fulton St", 2), ("WTC", 3)],
   "Fulton St": [("Wall St", 3), ("Cortlandt St", 3), ("Broadway", 2)],
   "Wall St": [("Brooklyn Bridge", 4), ("Fulton St", 3)],
   "Brooklyn Bridge": [("City Hall", 1), ("Wall St", 4), ("Chambers St", 2)],
   "City Hall": [("Brooklyn Bridge", 1), ("Broadway", 3)],
   "Broadway": [("Fulton St", 2), ("City Hall", 3), ("Times Sq", 4)],
   "Times Sq": [("Bryant Park", 2), ("Broadway", 4)],
   "Bryant Park": [("Times Sq", 2)]
}

#2024 #interview
"""

import heapq

def get_shortest_path(graph, start, end):
    distances = { key: float("inf") for key in graph.keys() }
    heap = [(0, start)]

    distances[start] = 0

    while len(heap) != 0:
        dist, node = heapq.heappop(heap)

        if node == end:
            break

        if dist > distances[node]:
            continue

        for child, weight in graph[node]:
            newDist = dist + weight

            if newDist < distances[child]:
                distances[child] = newDist
                heapq.heappush(heap, (newDist, child))

    return distances[end]


graph = {
   "WTC": [("Chambers St", 2), ("Cortlandt St", 3)],
   "Chambers St": [("Brooklyn Bridge", 2), ("WTC", 2)],
   "Cortlandt St": [("Fulton St", 2), ("WTC", 3)],
   "Fulton St": [("Wall St", 3), ("Cortlandt St", 3), ("Broadway", 2)],
   "Wall St": [("Brooklyn Bridge", 4), ("Fulton St", 3)],
   "Brooklyn Bridge": [("City Hall", 1), ("Wall St", 4), ("Chambers St", 2)],
   "City Hall": [("Brooklyn Bridge", 1), ("Broadway", 3)],
   "Broadway": [("Fulton St", 2), ("City Hall", 3), ("Times Sq", 4)],
   "Times Sq": [("Bryant Park", 2), ("Broadway", 4)],
   "Bryant Park": [("Times Sq", 2)]
}

print(get_shortest_path(graph, "WTC", "Bryant Park"))  # 13
