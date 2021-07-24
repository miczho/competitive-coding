import sys
from collections import defaultdict

input = sys.stdin.readline 

def chokudai():
    s = input()

    MOD = 10 ** 9 + 7
    word = ["c", "h", "o", "k", "u", "d", "a", "i"]
    freq = defaultdict(int)
    res = 0

    for ch in s:
        for i in range(8):
            if ch == word[i]:
                tmp = "".join(word[:i+1])
                freq[ch] += 1
                freq[tmp] += freq[tmp[:-1]]

    print(freq["chokudai"] % MOD)


if __name__ == '__main__':
    chokudai()