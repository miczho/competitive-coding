import sys

input = sys.stdin.readline

def diceCombo(n):
    dp = [0]*(n+1)

    dp[0] = 1
    for i in range(n+1):
        for j in range(1, 7):
            if i + j <= n: 
                dp[i + j] += dp[i]
                dp[i + j] %= 1_000_000_007

    return dp[n]


def main():
    print(diceCombo(int(input())))


if __name__ == '__main__':
    main()