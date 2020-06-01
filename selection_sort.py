def selection_sort(array):
    sorted_index = 0

    while sorted_index < len(array) - 1:  # if there is only one element in the unsorted array, the array is already
        # sorted
        mindex = sorted_index
        index = mindex + 1
        while index < len(array):
            if array[index] < array[mindex]:
                mindex = index
            index += 1
        if mindex == sorted_index:
            sorted_index += 1
        else:
            # swap elements at mindex and sorted_index
            tmp = array[mindex]
            array[mindex] = array[sorted_index]
            array[sorted_index] = tmp
            sorted_index += 1
    return array
