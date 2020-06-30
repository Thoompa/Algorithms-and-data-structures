class Node:
    data = None
    child = None

    def __init__(self, data):
        self.data = data

    def print(self):
        print(self.data)
        if self.child is not None:
            self.child.print()

    def add_child(self, new_child):
        if type(new_child) == type(self):
            if self.child is None:
                self.child = new_child
            else:
                self.child.add_child(new_child)
        else:
            raise TypeError


class LinkedList:
    length = 0
    root = None

    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, data):
        self.root.add_child(Node(data))

    def print(self):
        self.root.print()
