"""
https://medium.freecodecamp.org/how-and-why-you-should-use-python-generators-f6fb56650888

- Generators allow you to create iterators in a very pythonic manner.
- Iterators allow lazy evaluation, only generating the next element of an iterable object when requested. This is useful for very large data sets.
- Iterators and generators can only be iterated over once.
- Generator Functions are better than Iterators.
- Generator Expressions are better than Iterators (for simple cases only).

"""

def check_prime(number):
	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			return False
	return True

# Iterator
class Primes:
	def __init__(self, max):
		self.max = max
		self.number = 1
	def __iter__(self):
		return self
	def __next__(self):
		self.number += 1
		if self.number >= self.max:
			raise StopIteration
		elif check_prime(self.number):
			return self.number
		else:
			return self.__next__()

# Generator
# def Primes(max):
# 	number = 1
# 	while number < max:
# 		number += 1
# 		if check_prime(number):
# 			yield number
# primes = Primes(100)

# PEP 289 - Generator Expressions
primes = (i for i in range(2, 1000) if check_prime(i))

print(primes)
for x in primes:
	print(x)
print(primes)

for x in primes:
	if len(primes) == 0:
		print('Empty')
	print(x)

"""
https://docs.python.org/3/library/itertools.html
itertools
https://stackoverflow.com/a/8671323/5922564
https://stackoverflow.com/a/23069625/5922564
https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
"""