import sys

def main():
	a = [1, 2, 3]
	b = a.copy()
	b.append(4)
	print(a)
	print(b)

if __name__ == "__main__":
	main()