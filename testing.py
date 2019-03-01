import random
# def factorial(n):
# 	num = n
# 	if num == 0:
# 		return 1
# 	# 5! = 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2*1!
# 	return num * (factorial(num - 1))
		
# def fact(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * fact(n-1)

# print(factorial(5))


# memo ={}

# def fact(n):
#     if n in memo:
#         return memo[n]
#     elif n == 0:
#         return 1
#     else:
#         x = fact(n-1) * n
#         memo[n] = x
#         return x

# a = fact(5)
# b = fact(4)

# print(a,b)

#Maximum element in an array

def find_max_element(arr):
	max_element = arr[0]
	new_array = arr[1:]
	for c in new_array:
		if c > max_element:
			max_element = c
	return max_element, arr.index(max_element)


num_list = [11, 3, 5, 7, 100, 10]
# print(find_max_element(num_list))


# https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena

"""
On each loop iteration, insertion sort removes one element from the array. 
It then finds the location where that element belongs within another sorted array 
and inserts it there. It repeats this process until no input elements remain.
"""

def insertion_sort(arr, simulation=False):
	for i in range(len(arr)):
		cursor = arr[i]
		pos = i

		while pos > 1 and arr[pos - 1] > cursor:
			arr[pos] = arr[pos - 1]
			pos = pos - 1

		arr[pos] = cursor

	return arr

# print(insertion_sort(num_list))


