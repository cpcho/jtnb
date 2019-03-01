def binary_search(arr, item):
	first = 0
	last = len(arr) - 1
	found = False
	while first <= last and not found:
		mid = (first + last) // 2
		if arr[mid] == item:
			found = True
		else:
			if item < arr[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))