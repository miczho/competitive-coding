/**
 * https://leetcode.com/problems/closest-equal-element-queries/description/
 * 
 * #2025 #salesforce
 */

function solveQueries(nums: number[], queries: number[]): number[] {
  /**
   * 1. Iterate thru 'nums'
   * 2. For val = nums[i]
   *     1. If first occurrence then init instances[val] = [i, i]
   *     2. If second+ occurrence then
   *         1. closest[1st] = min(closest[1st], 1st + n - i)
   *         2. closest[last] = min(closts[last], i - last)
   *         3. closest[i] = min(i - last, 1st + n - i)
   *     3. Update last occurance (instances[val] = [1st, i])
   * 4. Iterate thru 'queries' and construct 'answer' using 'closest'
   */

  const n: number = nums.length;
  const instances: { [key: number]: number[] } = {};  // Value = [first occ, last occ]
  const closest: number[] = new Array(n).fill(Infinity);
  const answer: number[] = [];

  for (let i = 0; i < n; i++) {
    let val: number = nums[i];

    if (!(val in instances)) {
      instances[val] = [i, i];
      continue;
    }

    const first: number = instances[val][0];
    const last: number = instances[val][1];

    // Update distances in both directions
    closest[first] = Math.min(closest[first], first + n - i);  // New left dist
    closest[last] = Math.min(closest[last], i - last);  // New right dist
    closest[i] = Math.min(i - last, first + n - i);  // Left & right dist (may be updated later)

    instances[val][1] = i;
  }

  for (const query of queries) {
    answer.push(closest[query] !== Infinity ? closest[query] : -1);
  }

  return answer;
}
