def selection_sort(array):
    if not array:
        return array

    new_array = []

    while array != []:
        index_min = min(range(len(array)), key = array.__getitem__)

        new_array.append(array[index_min])
        del array[index_min]

    return new_array

def bubble_sort(array):
    if not array:
        return array

    length = len(array) - 1
  
    for index in range(length):
        for jndex in range(0, length - index):
            if array[jndex] > array[jndex + 1]:
                array[jndex], array[jndex + 1] = array[jndex + 1], array[jndex]

    return array

def count_sort(array, maximum = -1):
    if not array:
        return array


    return array
