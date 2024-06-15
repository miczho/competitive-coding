import sys
from collections import defaultdict
from string import ascii_lowercase

input = sys.stdin.readline

def add(val, need, k):
    if val % k: need -= k - (val % k)
    val += 1
    if val % k: need += k - (val % k)
    return (val, need)


def sub(val, need, k):
    if val % k: need -= k - (val % k)
    val -= 1
    if val % k: need += k - (val % k)
    return (val, need)


def kBeautyStr(n, k, s):
    if n % k: return -1
    
    freq = defaultdict(int)
    for c in s: freq[c] += 1
    
    ans, need = [ch for ch in s], 0
    for ch in ascii_lowercase:
        if freq[ch] % k: need += k - (freq[ch] % k)
    if not need: return s
    for i in range(n-1, -1, -1):
        freq[s[i]], need = sub(freq[s[i]], need, k)
        if need <= n - i:
            ans[i] = '#'
            stop = True
            for ch in ascii_lowercase:
                if ch <= s[i]: continue
                if not freq[ch] % k:
                    if need + k <= n - i:
                        ans[i] = ch
                        freq[ch], need = add(freq[ch], need, k)
                        break
                else:
                    ans[i] = ch
                    freq[ch], need = add(freq[ch], need, k)
                    break
            if ans[i] == '#': 
                stop = False
            else:
                for j in range(i+1, n):
                    if n-j > need:
                        ans[j] = 'a'
                    else:    
                        for ch in ascii_lowercase:
                            if freq[ch] % k:
                                ans[j] = ch
                                freq[ch], need = add(freq[ch], need, k)
                                break
            if stop: 
                break
        # print(freq)

    return ''.join(ans)




def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = input().strip()
        print(kBeautyStr(n, k, s))


if __name__ == '__main__':
    main()