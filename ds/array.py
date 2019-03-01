#https://stackoverflow.com/a/6667288/5922564
#[[0 for x in range(cols_count)] for x in range(rows_count)] 

N = 5
# Create a 1-D array

arr1 = [0] * N

#This is a better way
arr2 = [0 for i in range(N)]
print('arr1', arr1, 'arr2', arr2)
print()

# Define 2-D array
rows, cols = (N, N)

arr_2d_1 = [[0]*cols]*rows
arr_2d_1[0][0] = 1 #pointing to a single memory location
for row in arr_2d_1:
	print(row)
print(arr_2d_1[0] is arr_2d_1[1]) #False

# This is a better way
arr_2d_2 = [[0 for i in range(cols)] for j in range(rows)]
arr_2d_2[0][0] = 1
for row in arr_2d_2:
	print(row)
print(arr_2d_2[0] is arr_2d_2[1]) #False


"""
Diagonal Difference
https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
matrix = [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]]


def diagDiff(arr):
	l = len(arr[0])
	# ltr = []
	# rtl = []
	# for i in range(l):
	# 	ltr.append(arr[i][i])
	# for i in range(l-1, -1, -1):
	# 	rtl.append(arr[l-1-i][i])

	# Using List Comprehension
	ltr = [arr[i][i] for i in range(l)]
	rtl = [arr[l-1-i][i] for i in range(l-1,-1,-1)]
	return abs(sum(ltr) - sum(rtl))

print(diagDiff(matrix))


import itertools as IT

L = [  [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9] ]

N = len(L)
d = dict()
for i, j in IT.product(range(N), repeat=2):
	d.setdefault(j-1, []).append((i,j))

# print([[L[i][j] for i, j in d[k]] for k in range(-N+1, N)])