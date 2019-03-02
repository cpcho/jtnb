class HashTable:

	def __init__(self, size = 10):
		self.hash_table = [[] for _ in range(size)]
		self.key_exists = False

	def __repr__(self):
		return repr(self.hash_table)
	
	# https://stackoverflow.com/a/3611804/5922564
	def insert(self, key, value):
		bucket = self.bucket_generator(key)
		print('Bucket List', list(enumerate(bucket)))
		for i, kv in enumerate(bucket):
			k, v = kv
			if key == k:
				self.key_exists = True
				break
		if self.key_exists:
			print('key already exists.')
			bucket[i] = ((key, value))
		else:
			bucket.append((key, value))

	def search(self, key):
		bucket = self.bucket_generator(key)
		for i, kv in enumerate(bucket):
			k, v = kv
			if key == k:
				self.key_exists = True
		if self.key_exists:
			print('Key {0} exists. Value: {1}'.format(key, v))
			return ''
		else:
			print('Key {0} does not exist'.format(key))
			raise KeyError

	def delete(self, key):
		bucket = self.bucket_generator(key)
		for i, kv in enumerate(bucket):
			k, v = kv
			if key == k:
				del bucket[i]
				print('Key {0} is deleted.'.format(key))
				return ''
		print('Key {0} is not found.'.format(key))
		raise KeyError

	def bucket_generator(self, key):
		hash_key = hash(key) % len(self.hash_table)
		bucket = self.hash_table[hash_key]
		return bucket

ht = HashTable(25)
ht.insert(30, 'Henry')
ht.insert(1, 'Jiyon')
ht.insert(2, 'Together')
ht.insert(4, 'Random')
ht.insert(4, 'Haha')
print(ht)
print(ht.search(2))
print(ht.delete(4))
print(ht.delete(55))
print(ht)