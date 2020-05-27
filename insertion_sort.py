def insertion_sort(array):
    index = 1
    length = len(array)
    while index < length:
        new_index = index
        while array[new_index] < array[new_index - 1]:
            tmp = array[new_index]
            array[new_index] = array[new_index - 1]
            array[new_index - 1] = tmp
            if new_index == 1:
                break
            else:
                new_index -= 1
        index += 1
    return array


my_array = [1,6,3,34,7,4,5,7,45]
my_sorted_array = insertion_sort(my_array)
print(my_sorted_array)
