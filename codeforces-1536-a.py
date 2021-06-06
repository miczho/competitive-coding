import sys

input = sys.stdin.readline 

def gcd(a, b):
    while b != 0: a, b = b, a%b
    return a

def omkarAndBadStory(n, arr):
    arr.sort()
    if arr[0] < 0:
        print('NO')
        return

    val = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            val = min(val, gcd(arr[i], arr[j]))

    if((arr[-1] - arr[0]) // val + 1 > 300):
        print('NO')
    else:
        ans = list()
        for i in range(min(arr[0], 1), arr[-1]//val+1):
            ans.append(i * val)
        print('YES')
        print(len(ans))
        print(*ans)


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]

        omkarAndBadStory(n, arr)


main()