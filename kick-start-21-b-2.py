import sys

input = sys.stdin.readline
INF = float('-inf')

def longestProgression(n, arr):
    if n < 4:
        return n

    ans = 0
    diff = []
    for i in range(n-1):
        diff.append(arr[i+1] - arr[i])
    # print(diff)

    chunks = [INF]*(n-1)
    i = 0
    while i < n-1:
        j = i
        while j < n-1 and diff[i] == diff[j]:
            j += 1
        chunks[i], chunks[j-1] = j - i, j - i
        i = j
    # print(chunks)
    
    def check(c, d):
        ans = 0
        i = 0
        while i < n-1:
            j = i + c[i]
            if j < n-2 and ((d[j] + d[j+1]) == 2 * d[i]):
                if j < n-3 and d[j+2] == d[i]:
                    ans = max(ans, c[i] + c[j+2] + 2)
                else:
                    ans = max(ans, c[i] + 2)
            elif j < n-1:
                ans = max(ans, c[i] + 1)
            else:
                ans = max(ans, c[i])
            i = j
        return ans

    return max(check(chunks, diff), check(chunks[::-1], diff[::-1])) + 1


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        print(f'Case #{t+1}: {longestProgression(n, arr)}')


if __name__ == '__main__':
    main()