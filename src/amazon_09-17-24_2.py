"""
A user has provided an integer array called 'arr' of size 'n' and a
2-dimensional array called 'pairs' of size 'm' * 2. Each pair in 'pairs'
represents the starting and ending indices of a subarray within 'arr'.

For each subarray of 'arr' represented by the array pairs, the goal is to merge
and concatenate them into a new array called 'beautiful'.

The beauty of an element at index 'i' in 'arr' is defined as follows: if the
index 'i' has not contributed to the formation of the array 'beautiful', the
beauty is the count of integers in 'beautiful' that have a value strictly
smaller than 'arr[i]'. If the index 'i' has contributed to the formation of the
array 'beautiful', its beauty is 0.

Find the sum of the beauties of all the elements in the array 'arr'.

Example:

Input:
n = 6
arr = [1, 2, 3, 2, 4, 5]
m = 4
pairs = [[0, 1], [3, 4], [0, 0], [3, 4]]

Output:
12

#interview #2024
"""

def sumBeauties(n, arr, m, pairs):
    """
    Time complexity:
    Worst case 'beautiful' has m * n elements, and we have to sort 'beautiful'
    O((m * n) * log(m * n))

    Space complexity:
    Size of 'beautiful'
    O(m * n)
    """
    contributed = [False] * n
    beautiful = []
    result = 0

    for start, end in pairs:
        for i in range(start, end + 1):
            contributed[i] = True
            beautiful.append(arr[i])

    beautiful.sort()

    for i in range(n):
        if contributed[i]:
            continue

        lo, hi = -1, len(beautiful)

        while lo + 1 != hi:
            mid = lo + (hi - lo) // 2

            if beautiful[mid] < arr[i]:
                lo = mid
            else:
                hi = mid

        result += hi

    return result


n = 6
arr = [1, 2, 3, 2, 4, 5]
m = 4
pairs = [[0, 1], [3, 4], [0, 0], [3, 4]]
print(sumBeauties(n, arr, m, pairs))
