def merge_sort(array):
    middle_point = len(array) // 2 #get the middle point of the array so it can be divided by 2
    left_part = array[0: middle_point]
    right_part = array[middle_point:len(array)] #also works with array[middle_point:]

    print(array, left_part, right_part)
    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            pass
merge_sort([3, 4, 2, 7, 10, 5, 1])