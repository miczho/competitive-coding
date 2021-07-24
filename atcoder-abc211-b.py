import sys

input = sys.stdin.readline 

def cycleHit():
    arr = set()
    for i in range(4):
        arr.add(input().strip())
    print("Yes" if arr == {"2B", "3B", "H", "HR"} else "No")


if __name__ == '__main__':
    cycleHit()