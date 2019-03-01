# Example 1
squares = [x**2 for x in range(10)]
print(squares)
# equivalent to:
# squares = list(map(lambda x:x**2, range(10)))

# Example 2
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# equivalent to:
combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))
# note how the order of the for and if statements is the same in both these snippets.

vec = [-4, -2, 0, 2, 4]
print()
print([x*2 for x in vec]) #[-8, -4, 0, 4, 8]
print([x for x in vec if x >= 0]) #[0, 2, 4]
print([abs(x) for x in vec]) #[4, 2, 0, 2, 4]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print()
print([e.strip() for e in freshfruit])

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
print()
print([(x, x**2, -x) for x in range(6)])
#print([x, x**2 for x in range(6)]) # error

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print()
print([num for elem in vec for num in elem])

# equivalent to
#for elem in vec:
#	for num in elem:
#		print(num)

# complex expressions and nested functions:
from math import pi
print()
print([str(round(pi, i)) for i in range(1, 6)])


"""
Nested list comprehension
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
"""
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]
# transpose rows and columns:
print()
print([[row[i] for row in matrix] for i in range(4)])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# equivalent to:
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
# print(transposed)
# equivalent to:
transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
print(transposed)

"""
zip() function

Unpacking Argument Lists
https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
"""
print(list(zip(*matrix)))