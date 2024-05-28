from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        self.factorFreq = {}

        freqNums1 = Counter(nums1)
        freqNums2 = Counter(nums2)

        for n, freq in freqNums1.items():
            self.addToFactorFreq(n, freq)

        result = 0
        for n, freq in freqNums2.items():
            result += self.factorFreq.get(n * k, 0) * freq
        
        return result

    def addToFactorFreq(self, n, freq):
        i = 1
        while i * i <= n:
            if n % i == 0:
                self.factorFreq[i] = self.factorFreq.get(i, 0) + 1 * freq
                if n // i != i:
                    self.factorFreq[n // i] = self.factorFreq.get(n // i, 0) + 1 * freq
            i += 1
