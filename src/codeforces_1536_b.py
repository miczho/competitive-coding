import sys

input = sys.stdin.readline 

def prinzessinDerVerurteilung(n, s):
    strs = set()

    for i in range(n):
        for j in range(i+1, min(i+4, n+1)):
            strs.add(s[i:j])

    ans = []
    for i in range(26):
        ans.append(chr(ord('a') + i))
        tmp = ''.join(ans)
        if tmp not in strs:
            return tmp
        ans.pop()

    for i in range(26):
        ans.append(chr(ord('a') + i))
        for j in range(26):
            ans.append(chr(ord('a') + j))
            tmp = ''.join(ans)
            if tmp not in strs:
                return tmp
            ans.pop()
        ans.pop()

    for i in range(26):
        ans.append(chr(ord('a') + i))
        for j in range(26):
            ans.append(chr(ord('a') + j))
            for k in range(26):
                ans.append(chr(ord('a') + k))
                tmp = ''.join(ans)
                if tmp not in strs:
                    return tmp
                ans.pop()
            ans.pop()
        ans.pop()

    return -1


def main():
    for t in range(int(input())):
        n = int(input())
        s = input()

        print(prinzessinDerVerurteilung(n, s))


if __name__ == '__main__':
    main()