"""
#math #factors
"""

def gcd(a, b):
    while b != 0: a, b = b, a%b
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

def factors(n):
    i = 1
    factors = set()
    while i * i <= n:
        if not n % i:
            factors.add(i)
            factors.add(n // i)
        i += 1
    return factors