import sys

input = sys.stdin.readline

def increaseSubstr(n, s):
    ans = [1]
    for i in range(1, n):
        if s[i-1] < s[i]:
            ans.append(ans[-1]+1)
        else:
            ans.append(1)

    return ans


def main():
    for t in range(int(input())):
        n = int(input())
        s = input()
        ans = ' '.join((str(ch) for ch in increaseSubstr(n, s)))
        print(f'Case #{t+1}: {ans}')


if __name__ == '__main__':
    main()