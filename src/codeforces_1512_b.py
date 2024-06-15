import sys

input = sys.stdin.readline

def almostRect(n, arr):
    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*': ans.append([i, j])
            if len(ans) == 2: break

    if ans[0][0] == ans[1][0]:
        if ans[0][0] == 0:
            ans[0][0] += 1
        else:
            ans[0][0] -= 1
        arr[ans[0][0]][ans[0][1]] = '*'
        arr[ans[0][0]][ans[1][1]] = '*' 
    elif ans[0][1] == ans[1][1]:
        if ans[0][1] == 0:
            ans[0][1] += 1
        else:
            ans[0][1] -= 1
        arr[ans[0][0]][ans[0][1]] = '*'
        arr[ans[1][0]][ans[0][1]] = '*'
    else:
        arr[ans[0][0]][ans[1][1]] = '*'
        arr[ans[1][0]][ans[0][1]] = '*'

    return '\n'.join([''.join(a) for a in arr])


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [[ch for ch in input().strip()] for _ in range(n)]
        print(almostRect(n, arr))


if __name__ == '__main__':
    main()