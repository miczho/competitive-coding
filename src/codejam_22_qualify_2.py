import sys

input = sys.stdin.readline 

def printing(cmyk):
    cmyk[0][0] = min([arr[0] for arr in cmyk])
    cmyk[0][1] = min([arr[1] for arr in cmyk])
    cmyk[0][2] = min([arr[2] for arr in cmyk])
    cmyk[0][3] = min([arr[3] for arr in cmyk])

    if sum(cmyk[0]) < 10**6:
        return 'IMPOSSIBLE'
    else:
        res = ['0'] *4
        tmp = 10**6
        i = 0
        while tmp > 0:
            res[i] = str(cmyk[0][i]) if cmyk[0][i] <= tmp else str(tmp)
            tmp -= cmyk[0][i]
            i += 1
        return ' '.join(res)


def main():
    for t in range(int(input())):
        cmyk = []
        for _ in range(3):
            cmyk.append([int(x) for x in input().split()])
        print(f'Case #{t+1}: {printing(cmyk)}')


if __name__ == '__main__':
    main()