"""
#factors
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a
        b %= a
    return a

def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors