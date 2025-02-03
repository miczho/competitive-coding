/**
 * https://leetcode.com/problems/cheapest-flights-within-k-stops/
 * 
 * #favorite #2025 #revisit
 */

import java.util.*;

public class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dest, int k) {
        /**
         * TLE
         */

        Map<Integer, List<int[]>> graph = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return Integer.compare(a[0], b[0]);
        });

        for (int[] flight : flights) {
            graph.computeIfAbsent(flight[0], (x) -> new ArrayList<>()).add(new int[] { flight[1], flight[2] });
        }

        pq.offer(new int[] { 0, src, k + 1 });

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int price = node[0], city = node[1], stops = node[2];

            if (city == dest) {
                return price;
            }

            if (stops > 0) {
                for (int[] neighbor : graph.getOrDefault(city, new ArrayList<>())) {
                    int nextCity = neighbor[0], nextPrice = neighbor[1];
                    pq.offer(new int[] { price + nextPrice, nextCity, stops - 1 });
                }
            }
        }

        return -1;
    }
}
