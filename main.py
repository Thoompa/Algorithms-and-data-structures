# from insertion_sort import insertion_sort as sort
# from selection_sort import selection_sort as sort
from merge_sort import merge_sort as sort

print("Testing for merge_sort.py")

array = []  # empty array
sorted_array = sort(array.copy())
print("Unsorted array:", array, "\nSorted array:", sorted_array)

array = [24] # array with one element
sorted_array = sort(array.copy())
print("Unsorted array:", array, "\nSorted array:", sorted_array)

array = [7, 7, 7, 7, 5, 7, 7, 7]  # array with repeated value
sorted_array = sort(array.copy())
print("Unsorted array:", array, "\nSorted array:", sorted_array)

array = [1, 4, 7, 13, 29]  # already sorted array
sorted_array = sort(array.copy())
print("Unsorted array:", array, "\nSorted array:", sorted_array)

array = [6, 3, 10, 21, 8, 2/3, 0, -5, 6.3, 3**2]  # unsorted array
sorted_array = sort(array.copy())
print("Unsorted array:", array, "\nSorted array:", sorted_array)
