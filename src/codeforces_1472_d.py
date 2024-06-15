import sys, heapq

def evenOddGame(n, a):
	even, odd, bob, alice, turn = [], [], 0, 0, 1
	
	for i in a:
		if i & 1: heapq.heappush(odd, -i)
		else: heapq.heappush(even, -i)

	for i in range(n):
		if turn:
			if not odd or (even and even[0] <= odd[0]):
				alice -= heapq.heappop(even)
			else: heapq.heappop(odd)
		else:
			if not even or (odd and odd[0] <= even[0]):
				bob -= heapq.heappop(odd)
			else: heapq.heappop(even)
		turn ^= 1

	if alice > bob: return 'Alice'
	elif bob > alice: return 'Bob'
	else: return 'Tie'


def main():
    for _ in range(int(input())):
    	n, a = int(input()), [int(i) for i in input().split()]
    	print(evenOddGame(n, a))


if __name__ == "__main__":
    main()