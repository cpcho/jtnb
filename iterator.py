# https://docs.python.org/3/howto/functional.html#iterators

L = [1, 2, 3]
it = iter(L)
print(it) # <list_iterator object at 0x0000016A45568278>

print(it.__next__()) # 1, same as next(it)
print(next(it)) # 2
print(next(it)) # 3
# print(next(it))
"""
Traceback (most recent call last):
  File "iterator.py", line 7, in <module>
    print(next(it))
StopIteration
"""

# The two codes below are same:
for i in iter(L):
	print(i)

for i in L:
	print(i)

# Iterators can be materialized as lists or tuples by using 
# the list() or tuple() constructor functions:
L = [1, 2, 3]
iterator = iter(L)
t = tuple(iterator)
print(t) # (1, 2, 3)

L = [1, 2, 3]
iterator = iter(L)
a, b, c = iterator
print(a, b, c) # 1, 2, 3

"""
Note that you can only go forward in an iterator; 
there’s no way to get the previous element, reset the iterator, 
or make a copy of it. Iterator objects can optionally provide 
these additional capabilities, but the iterator protocol only 
specifies the __next__() method. Functions may therefore consume 
all of the iterator’s output, and if you need to do something different 
with the same stream, you’ll have to create a new iterator.
"""

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
	'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
for k in m:
	print(k, m[k])

"""
The dict() constructor can accept an iterator that returns a finite stream 
of (key, value) tuples:
"""
L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
print(dict(iter(L)))

"""
Files also support iteration by calling the readline() method until 
there are no more lines in the file. This means you can read each line 
of a file like this:
"""
# for line in file:
	# readline()
	# do somethin for each line

"""
Sets can take their contents from an iterable and let you iterate over 
the set’s elements:
"""

S = {2, 3, 5, 7, 11, 13}
for i in S:
	print(i)

# Generator expressions and list comprehensions
# https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions

line_list = ['  line 1\n', 'line 2  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list if line != "")
print(stripped_iter)
print(next(stripped_iter)) # line 1
print(next(stripped_iter)) # line 2

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list if line != ""]
print(stripped_list)


print([i**2 for i in range(5)])

