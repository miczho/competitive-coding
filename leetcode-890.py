class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        n = len(words[0])
        ans = []
        
        for word in words:
            forwardMap = {}
            backwardMap = {}
            valid = True
            for i in range(n):
                if pattern[i] not in forwardMap and word[i] not in backwardMap:
                    forwardMap[pattern[i]] = word[i]
                    backwardMap[word[i]] = pattern[i]
                elif pattern[i] in forwardMap and word[i] in backwardMap:
                    if forwardMap[pattern[i]] == word[i] and backwardMap[word[i]] == pattern[i]:
                        continue
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
            if valid:
                ans.append(word)
        
        return ans