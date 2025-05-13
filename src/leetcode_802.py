class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        node_type = [-1] * n  # -1, 0, 1

        def dfs(node, node_type, path=set()):
            if node in path:
                return 0

            is_safe = 1

            path.add(node)
            for child in graph[node]:
                if node_type[child] == -1:
                    is_safe &= dfs(child, node_type, path)
                else:
                    is_safe &= node_type[child]
            path.remove(node)

            node_type[node] = is_safe

            return is_safe

        ans = []
        for node in range(n):
            if node_type[node] == -1:
                dfs(node, node_type)

            if node_type[node] == 1:
                ans.append(node)

        return ans
