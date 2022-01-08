import sys

input = sys.stdin.readline 

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
 
    max_div = int(n ** 0.5 // 1)
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def complexMarketAnalysis(n, e, arr):
    ans = 0

    for i in range(n):
        if is_prime(arr[i]):
            j = i - e
            a, b = 0, 0
            while j >= 0 and arr[j] == 1:
                a += 1
                j -= e
            j = i + e
            while j < n and arr[j] == 1:
                b += 1
                j += e
            ans += (a + 1) * (b + 1) - 1 if a != 0 and b != 0 else a + b

    return ans


def main():
    for _ in range(int(input())):
        n, e = map(int, input().split())
        arr = [int(x) for x in input().split()]
        print(complexMarketAnalysis(n, e, arr))


if __name__ == '__main__':
    main()