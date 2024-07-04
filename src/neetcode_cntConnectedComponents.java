/**
 * Time Complexity:
 * O(N + N + M)
 * = O(N + M) where N = number of nodes and M = number of edges
 * 
 * Space Complexity:
 * O(N + N + M)
 * = O(N + M) where N = number of nodes and M = number of edges
 * NOTE: not too sure about this
 * 
 * https://neetcode.io/problems/count-connected-components
 * 
 * #2024
 */

class Solution {
    boolean[] visited;
    List<Integer>[] adjacent;

    public int countComponents(int n, int[][] edges) {
        // O(N) space
        visited = new boolean[n];
        // O(M) space - stores 2 * number of edges
        adjacent = new LinkedList[n];

        int result = 0;

        // O(N) time
        for (int i = 0; i < n; i++) {
            adjacent[i] = new LinkedList<>();
        }

        // O(M) time
        for (int[] e : edges) {
            adjacent[e[0]].add(e[1]);
            adjacent[e[1]].add(e[0]);
        }

        // O(N) time - visiting evey node exactly once
        for (int node = 0; node < n; node++) {
            if (visited[node] == false) {
                bfs(node);
                result++;
            }
        }

        return result;
    }

    void bfs(int start) {
        // O(N) space
        LinkedList<Integer> queue = new LinkedList<>();

        queue.add(start);
        while (queue.isEmpty() == false) {
            Integer currNode = queue.remove();

            for (Integer nextNode : adjacent[currNode]) {
                if (visited[nextNode] == false) {
                    queue.add(nextNode);
                }
            }

            visited[currNode] = true;
        }
    }
}





/**
 * Attempt 2: this problem can also be solved with union find
 * 
 * #revisit
 */
