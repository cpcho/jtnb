A= [
	[1,2,3,4,5,6],
	[1,2,3,4,5,6],
	[1,2,3,4,5,6],
	[1,2,3,4,5,6],
	[1,2,3,4,5,6],
	[1,2,3,4,5,6]
]



def max_square(arr):

	sum = []

	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1):
			sum.append(arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1])
	return max(sum)

print(max_square(A))