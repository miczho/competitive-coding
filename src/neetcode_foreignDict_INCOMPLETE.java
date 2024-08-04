/**
 * Unable to solve w/o looking at solution
 * 
 * https://neetcode.io/problems/foreign-dictionary
 * 
 * #2024 #blind75 #neetcode150 #revisit
 */

class Solution {
    public String foreignDictionary(String[] words) {
        int n = words.length;

        Map<Character, Character> seq = new HashMap<>();
        Set<Character> set = new HashSet<>();
        int prevMismatchIdx = Integer.MAX_VALUE;
        char head;

        for (int i = 0; i < n - 1; i++) {
            int j = i + 1;

            int iLen = words[i].length();
            int jLen = words[j].length();
            int idx = 0;

            while (idx < iLen && idx < jLen) {
                char iCh = words[i].charAt(idx);
                char jCh = words[j].charAr(idx);

                if (iCh == jCh) {
                    set.add(iCh);
                } else {
                    // if a ch exists in the seq, then insert middle
                    // else insert either head or tail
                }
                idx++;
            }

            while (idx < iLen || idx < jLen) {
                if (idx < iLen) {
                    char ch = words[i].charAt(idx);
                    if (!seq.containsValue(ch)) {
                        set.add(ch);
                    }
                }
                if (idx < jLen) {
                    char ch = words[j].charAt(idx);
                    if (!seq.containsValue(ch)) {
                        set.add(ch);
                    }
                }
                idx++;
            }
        }
    }
}
