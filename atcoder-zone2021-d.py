import sys
from collections import deque

input = sys.stdin.readline

def msgFromAliens(s):
    n, flip = len(s), 0
    ans = deque()
    for ch in s:
        if ch == 'R':
            flip ^= 1
            continue
        if flip:
            if ans and ch == ans[0]:
                ans.popleft()
            else:
                ans.appendleft(ch)
        else:
            if ans and ch == ans[-1]:
                ans.pop()
            else:
                ans.append(ch)

    if flip:
        ans.reverse()

    return ''.join(ans)


def main():
    s = input().strip()
    print(msgFromAliens(s))


if __name__ == '__main__':
    main()