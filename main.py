# from insertion_sort import insertion_sort as sort
# from selection_sort import selection_sort as sort
# from merge_sort import merge_sort as sort
from linked_list import LinkedList

print("Testing for linked_list.py")

my_list = LinkedList(5)
my_list.add_node(1)
my_list.add_node('hi')
my_list.add_node(-6)
my_list.print()
