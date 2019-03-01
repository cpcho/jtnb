#https://docs.python.org/3/library/collections.html


# OrderedDict
from collections import OrderedDict

roll_no = OrderedDict([
	(11, 'Henry'),
	(9, 'Jason'),
	(17, 'Justin')
])

for key, value in roll_no.items():
	print(key, value)
	"""
	11 Henry
	9 Jason
	17 Justin
	"""

# Default Dict
# Can contain duplicate keys
from collections import defaultdict

groups = [
	('Henry', 90),
	('Jason', 110),
	('Justin', 100),
	('Justin', 105),
	('Henry', 100)
]

dict_groups = defaultdict(list)

for key, value in groups:
	dict_groups[key].append(value)

print()
print(list(dict_groups.items()))
#[('Henry', [90, 100]), ('Jason', [110]), ('Justin', [100, 105])]
print()


# Counter
from collections import Counter

group_list = [
	('Henry', 90),
	('Jason', 110),
	('Justin', 100),
	('Justin', 105),
	('Henry', 100)
]

count = Counter(name for name, score in group_list)
print('Counter Example 1')
print(count) #Counter({'Henry': 2, 'Justin': 2, 'Jason': 1})

cnt_list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(cnt_list)

print()
print('Counter Example 2')
print(cnt[3]) #2
print()

# Counter::element()

cnt = Counter({1:3, 2:4})
print('Counter::element():')
print(list(cnt.elements())) #[1, 1, 1, 2, 2, 2, 2]
print()

# Counter::most_common()

cnt = Counter(cnt_list)
print('Counter::most_common():')
print(cnt.most_common()) #[(1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1), (8, 1)]
print()

# Counter::subtract()
cnt = Counter({1:3, 2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print('Counter::subtract():')
print(cnt) #Counter({1: 2, 2: 2})
print()


# Named Tuple
import collections

User = collections.namedtuple('User', 'name age gender')
henry = User(name='Henry', age=31, gender='M')
jason = User(name='Jason', age=30, gender='M')
print(henry) #User(name='Henry', age=31, gender='M')
print('Name of User: {0}'.format(henry.name)) #Name of User: Henry
print('Name of User: {0}'.format(jason.name)) #Name of User: Jason


# Deque
# Double-ended queue
# https://docs.python.org/3/library/collections.html#collections.deque
# https://www.geeksforgeeks.org/deque-in-python/
# https://www.geeksforgeeks.org/implement-stack-queue-using-deque/
import collections

lst = collections.deque()
lst.append('B')
lst.append('C')
lst.appendleft('A')
lst.insert(1, 'X')
print()
print(lst) #deque(['A', 'X', 'B', 'C'])
print()

name = collections.deque('henry')
print()
print('Deque: ', name) #Deque:  deque(['h', 'e', 'n', 'r', 'y'])
print('Queue length: ', len(name)) #Queue length:  5
print('Left part: ', name[0]) #Left part:  h
print('Right part: ', name[-1]) #Right part:  y
print()

name.remove('y')
print()
print('remove(b)', name) #remove(b) deque(['h', 'e', 'n', 'r'])
print()

name.extendleft('...')
name.append('-')

print()
print('Deque: ', name) #Deque:  deque(['.', '.', '.', 'h', 'e', 'n', 'r', '-'])
print()