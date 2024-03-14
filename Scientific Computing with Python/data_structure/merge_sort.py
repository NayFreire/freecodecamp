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
        if left_part[left_array_index] < right_part[right_array_index]: #If the number on the left is smaller than the right... 
            array[sorted_index] = left_part[left_array_index] #...the number on the left goes to its correct position...
            left_array_index += 1 #... and the left_array_index is incremented by 1, so it can go to the next position

        else: #If the number on the left is not smaller than the right... 
            array[sorted_index] = right_part[right_array_index] #...the number on the tight goes to its correct position...
            right_array_index += 1 #... and the right_array_index is incremented by 1, so it can go to the next position
            
        sorted_index += 1 # And after all, increment the sorted_index, so the next position in the array can be correctly assigned    
merge_sort([3, 4, 2, 7, 10, 5, 1])