class ListNode:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __repr__(self):
		return repr(self.data)

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def __repr__(self):
		nodes = []
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.next
		return '[' + ', '.join(nodes) + ']'

	def prepend(self, data):
		self.head = ListNode(data=data, next=self.head)

	def append(self, data):
		if not self.head:
			self.head = ListNode(data=data)
			print('if not self.head: self.head', self.head)
			return
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = ListNode(data=data)
		print('curr.next', curr.next)

	def find(self, key):
		curr = self.head
		while curr.data != key and curr:
			curr = curr.next
		return curr

	def remove(self, key):
		curr = self.head
		prev = None
		while curr.data != key and curr:
			prev = curr
			curr = curr.next
			print('while curr.data != key and curr: prev', prev, 'curr', curr)
		if prev is None:
			self.head = curr.next
			print('if prev is None: self.head', self.head)
		elif curr is not None:
			prev.next = curr.next
			curr.next = None #unlink
			print('elif curr is not None: curr', curr)

	def reverse(self):
		curr_node = self.head
		prev_node = None
		next_node = None
		while curr_node is not None:
			next_node = curr_node.next
			print('====================')
			print('next_node: ', next_node)
			curr_node.next = prev_node
			print('curr_node.next: ', curr_node.next)
			prev_node = curr_node
			print('prev_node', prev_node)
			curr_node = next_node
			print('curr_node', curr_node)
			print('====================')
		self.head = prev_node

new_list = SinglyLinkedList()
new_list.append(1)
new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
# new_list.append(4)
# new_list.append(5)

# new_list.remove(1)
print(new_list)
# print(new_list.find(4))
new_list.reverse()