import sys

def main():
    n = 50
    r = 25
 
    print(n, r)
    n ^= r
    r ^= n
    n ^= r
    print(n, r)

    
if __name__ == "__main__":
    main()