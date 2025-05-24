/**
 * The key is to realize that for consecutive 1 bits, it always cost less or equal
 * operations to remove by adding than by subtracting. 
 * 
 * https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/
 * 
 * #2025 #bits #greedy #salesforce
 */

function minOperations(n: number): number {
  let nCopy: number = n;
  let numOperations: number = 0;

  // Must iterate from right to left to account for updated bits
  for (let i = 0; i < 32; i++) {
    const currBit: number = (nCopy >> i) & 1;
    const nextBit: number = (nCopy >> (i + 1)) & 1;

    if (currBit === 0) {  // Skip if curr bit is 0
      continue;
    } else if (nextBit === 1) {  // Add if curr bit is 1 and next bit is 1
      nCopy += Math.pow(2, i);
    } else {  // Subtract if curr bit is 1 and next bit is 0
      nCopy -= Math.pow(2, i);
    }

    numOperations++;
  }

  return numOperations;
};
