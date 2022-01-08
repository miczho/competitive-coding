import sys

input = sys.stdin.readline 

def fairPlayoff(s):
    first = (0, 0); second = (0, 0)

    for i in range(4):
        if s[i] > first[0]:
            second = first
            first = (s[i], i+2)
        elif s[i] > second[0]:
            second = (s[i], i+2)

    if (first[1] // 2 == 1 and second[1] // 2 == 2):
        return 'YES'
    elif (first[1] // 2 == 2 and second[1] // 2 == 1):
        return 'YES'
    return 'NO'


def main():
    for t in range(int(input())):
        s = [int(i) for i in input().split()]

        print(fairPlayoff(s))


if __name__ == '__main__':
    main()