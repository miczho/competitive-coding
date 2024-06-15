import sys

def painter(n, p):
    valid = [set(['R', 'O', 'P', 'A']), set(['Y', 'O', 'G', 'A']), set(['B', 'P', 'G', 'A'])]
    ans = 0

    for a in valid:
        paint = False
        for b in p:
            if b in a and not paint:
                paint = True
                ans += 1
            elif b not in a and paint:
                paint = False

    return ans

def main():
    for t in range(int(input())):
        n = int(input())
        p = input()
        print(f'Case #{t+1}: {painter(n, p)}')

if __name__ == '__main__':
    main()