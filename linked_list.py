"""
http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
A reference to None will denote the fact that there is no next node.

It is very important to note that the list class itself does not contain any 
node objects. Instead it contains a single reference to only the first node in 
the linked structure.

"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

class UnorderedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current != None:
            nodes.append(repr(current))
            current = current.get_next()
        return '[' + ', '.join(nodes) + ']'

    def is_empty(self):
        # checks to see if the head of the list is a reference to None
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    # Linked list traversal

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            # If the item to be removed happens to be the first item in the list, 
            # then current will reference the first node in the linked list. 
            # This also means that previous will be None.
            self.head = current.get_next()
        else:
            # if previous is not None, the node to be removed is somewhere down the 
            # linked list structure
            previous.set_next(current.get_next())

    def append(self, item):
        temp = Node(item)
        if not self.head:
            self.head = temp
            return
        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(temp)

my_list = UnorderedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.append(100)

print(my_list)