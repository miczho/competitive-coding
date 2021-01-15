import sys

def correctPlacement(n, fren):
	fren.sort()
	ans = ['-1']*n

	j = 0
	k = -1
	for i in range(n):
		while fren[j][0] != fren[i][0]:
			if k == -1 or fren[j][1] < fren[k][1]:
				k = j
			j += 1
		if k != -1 and fren[k][1] < fren[i][1]:
			ans[fren[i][2]-1] = str(fren[k][2])
	print(' '.join(ans))


def main():
    for t in range(int(input())):
    	n = int(input())
    	fren = []
    	for i in range(1, n+1):
    		h, w = map(int, input().split())
    		if h > w: fren.append([h, w, i])
    		else: fren.append([w, h, i])
    	correctPlacement(n, fren)

if __name__ == "__main__":
    main()