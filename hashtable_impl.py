"""
Hash Table Implementation
http://paulmouzas.github.io/2014/12/31/implementing-a-hash-table.html
http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/

Two ways for collision resolution:
	1. Linear probing
	2. Chaining (preferred)

Standard Implementation of Hash Table with Python Using Python's 
built-in hash() function
"""
hash_table = [[] for _ in range(10)]

"""
While inserting a new element into the hash table, we first search 
if the key already exists in the hash table.

– If the key is already present in the hash table, then we update its 
value with the new one.
– Otherwise, we insert a new key-value pair into the hash table.
"""
def insert(hash_table, key, value):
	hash_key = hash(key) % len(hash_table)
	key_exists = False
	bucket = hash_table[hash_key]
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			key_exists = True
			print('if key exists, the i is:', i)
			break
	if key_exists:

		bucket[i] = ((key, value))
		
	else:
		bucket.append((key, value))

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print()
print (hash_table)
# [[(10, 'Nepal'), (20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]

"""
While searching for any key in the hash table, we have to loop through 
each individual sublist.
"""
def search(hash_table, key):
	hash_key = hash(key) % len(hash_table)
	bucket = hash_table[hash_key]
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return v
print(search(hash_table, 10)) # Nepal

"""
While deleting any existing element from the hash table, we first search if the key 
already exists in the hash table.

– If the key is present (found) in the hash table, then we simply delete it. We delete 
that particular key-value pair from the hash table.
– Otherwise, no operation is done. We can simply print a message saying that the key was 
not found in the hash table.
"""
def delete(hash_table, key):
	hash_key = hash(key) % len(hash_table)
	key_exists = False
	bucket = hash_table[hash_key]
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			key_exists = True
			break
	if key_exists:
		del bucket[i]
		print('Key {0} deleted'.format(key))
	else:
		print('key {0} not found'.format(key))
delete(hash_table, 10)
delete(hash_table, 100)
