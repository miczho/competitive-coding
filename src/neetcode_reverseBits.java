/**
 * Note that this problem will convert from signed to unsigned int for you
 * 
 * https://neetcode.io/problems/reverse-bits
 * 
 * #2024
 */

class Solution {
    public int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; i++) {
            int mask = (n >> i) & 1;
            result |= mask << (31 - i);
        }

        return result;
    }
}
