class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def parChecker(SymbolString):
	s = Stack()
	balanced = True
	index = 0
	while balanced and index < len(SymbolString):
		symbol = SymbolString[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(o, c):
	opening = "([{"
	closing = ")]}"
	return opening.index(o) == closing.index(c)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))