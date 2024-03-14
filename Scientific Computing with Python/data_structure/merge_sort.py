def merge_sort(array):
    middle_point = len(array) // 2 #get the middle point of the array so it can be divided by 2
    left_part = array[0: middle_point]
    right_part = array[middle_point:len(array)] #also works with array[middle_point:]
    
    print(array, middle_point, array[middle_point], left_part, right_part)

merge_sort([3, 4, 2, 7, 10, 5, 1])