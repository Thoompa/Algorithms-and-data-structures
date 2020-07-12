# from insertion_sort import insertion_sort as sort
# from selection_sort import selection_sort as sort
# from merge_sort import merge_sort as sort
# from linked_list import LinkedList
from binary_tree import Node

print("Testing for binary_tree.py")

bst = Node(15)
print(bst.is_full())
bst.insert(8)
print(bst.is_full())
bst.insert(17)
print(bst.is_full())
bst.insert(16)
print(bst.is_full())
bst.insert(18)
print(bst.is_full())
bst.print_in_order()
bst.print_pre_order()
bst.print_post_order()
bst.delete(17)
bst.print_pre_order()
print(bst.search(18))
print(bst.search(19))
