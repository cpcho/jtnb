#https://www.puzzlr.org/understanding-kadanes-algorithm-maximum-subarray-problem/
sample = [3,5,-2,-1,5,3,1]
def max_subarray(arr):
	prev_subarray_sum = max_so_far = arr[0]
	for i in arr[1:]:
		prev_subarray_sum = max(prev_subarray_sum, 0) + i
		max_so_far = max(max_so_far, prev_subarray_sum)
	return max_so_far

print(max_subarray(sample))