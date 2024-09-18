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

#interview
"""

def sumBeauties(n, arr, m, pairs):
    pass
