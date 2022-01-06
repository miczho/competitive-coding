import sys

input = sys.stdin.readline 

def yearOfCow(n, arr):
    zodiac = {
        "Ox": 0, 
        "Tiger": 1, 
        "Rabbit": 2, 
        "Dragon": 3, 
        "Snake": 4, 
        "Horse": 5, 
        "Goat": 6,
        "Monkey": 7, 
        "Rooster": 8,
        "Dog": 9,
        "Pig": 10,
        "Rat": 11
    }
    cows = {"Bessie": 0}

    for _ in range(110):
        for a in arr:
            if a[-1] in cows:
                cows[a[0]] = cows[a[-1]]
                curr = cows[a[-1]] % 12
                if a[3] == "next":
                    if curr >= zodiac[a[4]]:
                        cows[a[0]] += 12 - curr + zodiac[a[4]]
                    else:
                        cows[a[0]] += zodiac[a[4]] - curr
                else:
                    if curr <= zodiac[a[4]]:
                        cows[a[0]] += -12 - curr + zodiac[a[4]]
                    else:
                        cows[a[0]] += zodiac[a[4]] - curr

    return abs(cows["Elsie"])


def main():
    n = int(input())
    arr = [[w for w in input().split()] for _ in range(n)]

    print(yearOfCow(n, arr))


if __name__ == '__main__':
    main()
