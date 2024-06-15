/**
 * Use a min heap storing (char value, reverse index)
 * Loop through the string - pop heap if char is '*', append heap is char is not '*'
 * 
 * Solution was BARELY accepted:
 * https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/submissions/1286274270/
 * 
 * Time Complexity:
 * O(NlogN + N + NlogN)
 * = O(NlogN) where N = length of 's'
 * 
 * Space Complexity:
 * O(N + N)
 * = O(N) where N = length of 's'
 * 
 * https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
 * 
 * #2024
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    private int n;

    public String clearStars(String s) {
        n = s.length();

        Comparator<HashMap<String, Integer>> comparator = (map1, map2) -> {
            int charValue1 = map1.get("charValue");
            int charValue2 = map2.get("charValue");

            // First, compare the chars
            if (charValue1 != charValue2) {
                return Integer.compare(charValue1, charValue2);
            }

            // If the chars are the same, compare the indices
            int reverseIdx1 = map1.get("reverseIdx");
            int reverseIdx2 = map2.get("reverseIdx");
            return Integer.compare(reverseIdx1, reverseIdx2);
        };
        // O(N) space
        PriorityQueue<HashMap<String, Integer>> minHeap = new PriorityQueue<>(comparator);

        // O(NlogN) time
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);

            if (ch == '*') {
                minHeap.poll();
            } else {
                HashMap<String, Integer> chEntry = new HashMap<>();

                chEntry.put("charValue", (int) ch);
                chEntry.put("reverseIdx", this.getReversedIdx(i));
                minHeap.add(chEntry);
            }
        }

        // O(N) space
        char[] result = new char[this.n];

        // O(N) time
        Arrays.fill(result, '_');
        // O(NlogN) time
        while (!minHeap.isEmpty()) {
            HashMap<String, Integer> chEntry = minHeap.poll();
            
            result[this.getReversedIdx(chEntry.get("reverseIdx"))] = (char) (int) chEntry.get("charValue");
        }

        return new String(result).replace("_", "");
    }

    private int getReversedIdx(int i) {
        return this.n - 1 - i;
    }
}





/**
 * Attempt 2 - small optimizations
 * 
 * Same complexity but different data structures and reduced passes brings time down a lot:
 * https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/submissions/1286329878/
 */

import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    private int n;

    public String clearStars(String s) {
        n = s.length();

        Comparator<int[]> comparator = (a, b) -> {
            return a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]);
        };
        // O(N) space
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(comparator);
        // O(N) space
        char[] sArr = s.toCharArray();

        // O(NlogN) time
        for (int i = 0; i < n; i++) {
            char ch = sArr[i];

            if (ch == '*') {
                int[] charEntry = minHeap.poll();
                sArr[this.getReversedIdx(charEntry[1])] = '*';
            } else {
                int[] charEntry = { (int) ch, this.getReversedIdx(i) };
                minHeap.add(charEntry);
            }
        }

        return new String(sArr).replace("*", "");
    }

    private int getReversedIdx(int i) {
        return this.n - 1 - i;
    }
}
