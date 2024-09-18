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


def sumBeauties2(n, arr, m, pairs):
    """
    Time complexity:
    Cost of sorting 'arr' to build 'parsedArr'
    O(n * log n)

    Space complexity:
    Size of 'parsedArr' == 'contributed' == 'freq' == 'beauty'
    O(n)
    """
    parsedArr = sorted((num, i) for i, num in enumerate(arr))
    contributed = [0] * (n + 1)  # how often an element INDEX is used in 'beautiful'
    freq = {}  # how often an element VALUE is used in 'beautiful'
    beauty = {}
    result = 0

    # Set up 'contributed'
    for start, end in pairs:
        contributed[start] += 1
        contributed[end + 1] -= 1

    # Build 'contributed' and 'freq'
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]] = 0

        freq[arr[i]] += contributed[i]
        contributed[i + 1] += contributed[i]

    beauty[parsedArr[0][0]] = 0  # Beauty of smallest element is always 0

    # TODO: debugging
    print(arr)
    print(pairs)
    print("idx", parsedArr[0][1], "num", parsedArr[0][0], "contributed", contributed[parsedArr[0][1]], "beauty", beauty[parsedArr[0][0]])

    for i in range(1, n):
        num, idx = parsedArr[i]
        prevNum = parsedArr[i - 1][0]

        # Only need to calc beauty of diff value elements
        # Beauty of same value elements are equal
        if num != prevNum:
            # Beauty = Beauty of prev num + Freq of prev num in 'beautiful'
            beauty[num] = beauty[prevNum] + freq[prevNum]

        # Only add beauty if not contributed to 'beautiful'
        if contributed[idx] == 0:
            result += beauty[num]

        # TODO: debugging
        print("idx", idx, "num", num, "contributed", contributed[idx], "beauty", beauty[num])

    return result



n = 6
arr = [1, 2, 3, 2, 4, 5]
m = 4
pairs = [[0, 1], [3, 4], [0, 0], [3, 4]]
print(sumBeauties(n, arr, m, pairs))
print(sumBeauties2(n, arr, m, pairs))
