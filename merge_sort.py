"""
Merge sort is a perfectly elegant example of a Divide and Conquer algorithm. 
It simple uses the 2 main steps of such an algorithm:

(1) Continuously divide the unsorted list until you have N sublists, where each sublist 
has 1 element that is “unsorted” and N is the number of elements in the original array.

(2) Repeatedly merge i.e conquer the sublists together 2 at a time to produce new sorted 
sublists until all elements have been fully merged into a single sorted array.
"""
def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1

		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k] = R[j]
			j+=1
			k+=1
	return arr

num_list = [1, 11, 3, 5, 2, 10]
print(mergeSort(num_list))


# No Class Version
def merge_sort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	# Perform merge_sort recursively on both halves
	L, R = merge_sort(arr[:mid]), merge_sort(arr[mid:])

	# Merge each side together
	return merge(L, R, arr.copy())

def merge(l, r, merged):
	l_cursor, r_cursor = 0, 0
	while l_cursor < len(l) and r_cursor < len(r):

		# Sort each one and place into the result
		if l[l_cursor] <= r[r_cursor]:
			merged[l_cursor + r_cursor] = l[l_cursor]
			l_cursor += 1
		else:
			merged[l_cursor + r_cursor] = r[r_cursor]
			r_cursor += 1

	for l_cursor in range(l_cursor, len(l)):
		merged[l_cursor + r_cursor] = l[l_cursor]

	for r_cursor in range(r_cursor, len(r)):
		merged[l_cursor + r_cursor] = r[r_cursor]

	return merged

num_list = [11, 3, 5, 2, 10]
print(merge_sort(num_list))

# Class MergeSort
class MergeSort:
	def __init__(self):
		self.round = 0

	def merge_sort(self, arr):
		if len(arr) <= 1:
			return arr

		mid = len(arr) // 2
		# Perform merge_sort recursively on both halves
		left, right = self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:])

		# Tracking purposes
		self.round += 1
		print('Round', self.round)
		print('After merge:')
		print('left:', left, 'right:', right)
		print()

		# Merge each side together
		return self.merge(left, right, arr.copy())

	def merge(self, left, right, merged):

		left_cursor, right_cursor = 0, 0

		while left_cursor < len(left) and right_cursor < len(right):

			# Sort each one and place into the result
			if left[left_cursor] <= right[right_cursor]:
				merged[left_cursor + right_cursor] = left[left_cursor]
				print('Case 1: merged[left_cursor + right_cursor] = left[left_cursor]')
				print('left_cursor:', left_cursor, 'right_cursor:', right_cursor)
				print()
				left_cursor += 1
			else:
				merged[left_cursor + right_cursor] = right[right_cursor]
				print('Case 2: merged[left_cursor + right_cursor] = right[right_cursor]')
				print('left_cursor:', left_cursor, 'right_cursor:', right_cursor)
				print()
				right_cursor += 1

		for left_cursor in range(left_cursor, len(left)):
			merged[left_cursor + right_cursor] = left[left_cursor]

		for right_cursor in range(right_cursor, len(right)):
			merged[left_cursor + right_cursor] = right[right_cursor]

		return merged

num_list = [11, 3, 5, 1, 2, 10]
merge_and_sort = MergeSort()
# print(merge_and_sort.merge_sort(num_list))