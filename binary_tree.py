class Node:
    left_child = None
    right_child = None
    data = None
    isFull = False

    def __init__(self, data):
        self.data = data
        self.isFull = True

    def insert(self, number):
        # if new number is less than or equal to my number, make it a left child
        if number <= self.data:
            if self.left_child is None:
                # if I don't have a left child, new number is my left child
                self.left_child = Node(number)
                if self.right_child is None:
                    # I have no right child so I am no longer full
                    self.isFull = False
                else:
                    # I am only full if my right child is full
                    self.isFull = self.right_child.is_full()
            else:
                # I already have a left child, so send the new number down
                self.left_child.insert(number)
                # if I had no right child, I was not full and I am still not full
                if self.right_child is not None:
                    # I am only full if my right child is full and my left child is full
                    if self.right_child.is_full():
                        self.isFull = self.left_child.is_full()
        else:
            # the new number is bigger than me so make it a right child
            if self.right_child is None:
                # I have no right child so just make it a right child
                self.right_child = Node(number)
                if self.left_child is None:
                    # I have no left child so I am no longer full
                    self.isFull = False
                else:
                    # I am only full if my left child is also full
                    self.isFull = self.left_child.is_full()
            else:
                # I already have a right child, so send the new number down
                self.right_child.insert(number)
                # if I had no left child, I was not full and I am still not full
                if self.left_child is not None:
                    # I am only full if my left child is full and my right child is full
                    if self.left_child.is_full():
                        self.isFull = self.right_child.is_full()


    def print_in_order(self):
        if self.left_child is not None:
            self.left_child.print_in_order()
        print(self.data)
        if self.right_child is not None:
            self.right_child.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left_child is not None:
            self.left_child.print_pre_order()
        if self.right_child is not None:
            self.right_child.print_pre_order()

    def print_post_order(self):
        if self.left_child is not None:
            self.left_child.print_post_order()
        if self.right_child is not None:
            self.right_child.print_post_order()
        print(self.data)

    def search(self, number):
        if self.data == number:
            return True
        elif number < self.data:
            if self.left_child is None:
                return False
            else:
                return self.left_child.search(number)
        else:
            if self.right_child is None:
                return False
            else:
                return self.right_child.search(number)

    def is_full(self):
        return self.isFull

    def get_list(self):
        pass

    def delete(self, num):
        # Assume delete is never run on the root of a single node tree
        if num == self.data:
            # I am the root of the tree
            if self.right_child is None:
                return self.left_child
            elif self.left_child is None:
                return self.right_child
            else:
                leftmost_right_child = self.right_child
                if leftmost_right_child.left_child is None:
                    self.data = leftmost_right_child.data
                    self.right_child = None
                    return True
                while leftmost_right_child.left_child is not None:
                    parent = leftmost_right_child
                    leftmost_right_child = leftmost_right_child.left_child
                self.data = leftmost_right_child.data
                parent.left_child = None
            return True
        else:
            if self.right_child is not None:
                self.right_child.delete(num)
            if self.left_child is not None:
                self.left_child.delete(num)
