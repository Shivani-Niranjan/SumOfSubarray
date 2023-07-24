'''
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.

PS: A subarray sum denotes the sum of all the elements of that subarray.

Input
A = [1, 2, 3]

Output
20

Input
A = [2, 1, 3]

Output
19
'''

array = list(map(int, input().strip().split()))
sum = 0
for i in range(len(array)):
    sum += array[i] * (i + 1) * (len(array) - i)
print(sum)
