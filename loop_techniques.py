"""
looping technique
https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)
"""
enumerate
When looping through a sequence, the position index and corresponding value 
can be retrieved at the same time using the enumerate() function.
https://docs.python.org/3/library/functions.html#enumerate
"""
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))

#equivalent to:
def enumerate(sequence, start=0):
	n = start
	for e in sequence:
		yield n, e
		n += 1

"""
zip() function
To loop over two or more sequences at the same time, the entries can be paired 
with the zip() function.
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))

"""
reversed() function
"""
for i in reversed(range(1, 10, 2)):
	print(i) # 9 7 5 3 1

"""
It is sometimes tempting to change a list while you are looping over it; however, 
it is often simpler and safer to create a new list instead.
"""
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for v in raw_data:
	if not math.isnan(v):
		filtered_data.append(v)
print(filtered_data)