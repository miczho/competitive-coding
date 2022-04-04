import sys

input = sys.stdin.readline 

def punchedCards(r, c):
    res = []

    res.append('..+' + ('-+' * (c-1)))
    res.append('..|' + ('.|' * (c-1)))

    for i in range((r-1)*2+1):
        if i % 2 == 0:
            res.append('+-+' + ('-+' * (c-1)))
        else:
            res.append('|.|' + ('.|' * (c-1)))

    return res


def main():
    for t in range(int(input())):
        r, c = map(int, input().split())
        print(f'Case #{t+1}:')
        print('\n'.join(punchedCards(r, c)))


if __name__ == '__main__':
    main()