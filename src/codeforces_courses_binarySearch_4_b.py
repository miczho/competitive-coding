import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def minAveragePath(n, m, to, weight, graph):
	def f(m):
		new_weight = []
		for i in weight:
			new_weight.append(i - m)
		dist = [10**9]*(n+1)
		dist[1] = 0
		pre = [-1]*(n+1)
		pre[1] = 0
		# print(new_weight)
		# print(dist)

		q = [1]
		while q:
			new_q = []
			for i in q:
				for j in graph[i]:
					if dist[to[j]] == 10**9 or dist[i] + new_weight[j] < dist[to[j]]:
						dist[to[j]] = dist[i] + new_weight[j]
						new_q.append(to[j])
						pre[to[j]] = i
			q = new_q
		# print(dist)

		if pre[n] != -1 and dist[n] <= 0:
			curr = n
			ans = deque()
			# print(pre)
			while pre[curr] != -1:
				ans.appendleft(curr)
				curr = pre[curr]
			return(list(ans))
		return []

	l = 0
	r = 10**9+1
	ans = []
	for _ in range(70):
		m = (l + r) / 2
		# print(m)
		tmp = f(m)
		if tmp:
			r = m
			ans = tmp
		else:
			l = m
 
	# print(r)
	if r != 10**9:
		print(len(ans)-1)
		print(*ans)
	else:
		print(-1)



def main():
	n, m = map(int, input().strip().split())
	to = []
	weight = []
	graph = defaultdict(list)
	for i in range(m):
		a, b, c = map(int, input().strip().split())
		to.append(b)
		weight.append(c)
		graph[a].append(len(to)-1)
	minAveragePath(n, m, to, weight, graph)


if __name__ == '__main__':
	main()