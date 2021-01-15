from random import randint

print(1)
n, m = randint(100_000, 2 * 100_000), randint(100_000, 2 * 100_000) 
print(str(n) + " " + str(m))
s = ''
for i in range(n):
	if randint(0, 1):
		s += '+'
	else: s += '-'
print(s)

for i in range(m):
	l = randint(1, n)
	r = randint(l, n)
	print(str(l) + " " + str(r))