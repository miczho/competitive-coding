/**
 * Time Complexity:
 * O(Nlog(N) + N*M)
 * = O(N*M), where N = length of rewardValues, M = largest reward
 * 
 * NOTE:
 * the solution is O(N^2) but not little-o o(N^2) because `lim_N->infinity ((Nlog(N) + N^2) / N^2) = 1`
 * o(N^2) must be satisfied (i.e. approach a value < 1) to solve this problem:
 * https://leetcode.com/problems/maximum-total-reward-using-operations-ii/
 * 
 * ABOUT LITTLE-O:
 * `f(N) = o(g(N))` means `lim_N->infinity (f(N) / g(N)) < 1`
 * 
 * Space Complexity:
 * O(2*M)
 * = O(M), where M = largest reward
 * 
 * https://leetcode.com/problems/maximum-total-reward-using-operations-i/
 * 
 * #2024 #littleO
 */

/**
 * @param {number[]} rewardValues
 * @return {number}
 */
var maxTotalReward = function(rewardValues) {
    // by default x = 0 is valid
    // O(2*M) space because the largest possible value is (largest reward - 1) + (largest reward)
    let validX = new Set([0])
    let result = 0

    // O(Nlog(N)) time
    rewardValues.sort((a, b) => a - b)

    // O(N*M) time
    for (const reward of rewardValues) {
        for (const x of validX) {
            if (x < reward) {
                validX.add(x + reward)
                result = Math.max(result, x + reward)
            }
        }
    }

    return result
}
