"""
#factors
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def prime_factors(n):
    result = []

    # check for 2
    while n % 2 == 0:
        result.append(2)
        n //= 2

    # check for odd values up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 2

    # if n > 1, then it's a prime
    if n > 1:
        result.append(n)

    return result

def factors(n):
    result = set()
    
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.add(i)
            result.add(n // i)
        i += 1

    return result