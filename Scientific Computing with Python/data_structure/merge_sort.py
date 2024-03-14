def merge_sort(array):
    middle_point = len(array) // 2 #get the middle point of the array so it can be divided by 2
    print(array, middle_point, array[middle_point])

merge_sort([3, 4, 2, 7, 10, 5, 1])