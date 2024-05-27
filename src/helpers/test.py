from collections import Counter

# Define two Counters
counter1 = Counter({'a': 3, 'b': 2, 'c': 1})
counter2 = Counter({'a': 4, 'b': 1, 'd': 1})

# Subtract counter2 from counter1
result = counter1 - counter2

print("Result of subtracting counter2 from counter1:", result)
