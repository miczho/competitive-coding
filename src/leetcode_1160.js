/**
 * https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
 * 
 * #2025 #payPal
 */


/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function (words, chars) {
  const getFreqMap = (str) => {
    const freq = {};

    for (const ch of str) {
      freq[ch] = (freq[ch] ?? 0) + 1;
    }

    return freq;
  };

  const charsFreq = getFreqMap(chars);
  let result = 0;

  for (const word of words) {
    const wordFreq = getFreqMap(word);
    let canForm = true;

    for (const ch in wordFreq) {
      if ((charsFreq[ch] ?? 0) < wordFreq[ch]) {
        canForm = false;
        break;
      }
    }

    if (canForm) {
      result += word.length;
    }
  }

  return result;
};
