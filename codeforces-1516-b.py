import sys

input = sys.stdin.readline 

def AGAGAXOOORRR(n, arr):
    psum = [0]

    for i in arr:
        psum.append(psum[-1] ^ i)

    for i in range(n-1):
        if psum[i+1] == psum[i+1] ^ psum[-1]:
            return 'YES'

    for i in range(n-1):
        for j in range(i+1, n-1):
            if psum[i+1] == psum[i+1] ^ psum[j+1] and psum[i+1] == psum[j+1] ^ psum[-1]:
                return 'YES'

    return 'NO'


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]

        print(AGAGAXOOORRR(n, arr))


if __name__ == '__main__':
    main()