import sys

input = sys.stdin.readline
valid = {'0': '0', '1': '1', '2': '5', '5': '2', '8': '8'}

def convert(n):
    n = str(n).zfill(2)
    n = ''.join((valid[i] for i in n))
    return int(n[::-1])


def isValid(n):
    for c in str(n):
        if c not in valid:
            return False
    return True


def planetLapituletti(h, m, s1, s2):
    ans = ['00', '00']

    for i in range(s1, h):
        stop = False
        if isValid(i) and convert(i) < m:
            ans[0] = str(i).zfill(2)
            if int(ans[0]) == s1:
                for j in range(s2, m+1):
                    if j == m: 
                        ans[0] = '00'
                    elif isValid(j) and convert(j) < h:
                        ans[1] = str(j).zfill(2)
                        stop = True
                        break
            else: stop = True
        if stop: break

    return ':'.join(ans)


def main():
    for t in range(int(input())):
        h, m = map(int, input().split())
        s1, s2 = map(int, input().split(':'))
        print(planetLapituletti(h, m, s1, s2))


if __name__ == '__main__':
    main()