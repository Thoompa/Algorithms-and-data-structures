class Node:
    data = None
    child = None

    def __init__(self, data):
        self.data = data

    def add_child(self, new_child):
        if type(new_child) == type(self):
            if new_child is None:
                self.child = new_child
            else:
                self.child.add_child(new_child)
        else:
            raise TypeError


class LinkedList:
    length = 0
    root = None

    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add_child(Node(data))


my_list = LinkedList
my_list.add_node(1)
my_list.add_node('hi')
my_list.add_node()
