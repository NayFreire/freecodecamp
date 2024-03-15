def merge_sort(array):
    if len(array) <= 1: # the minimal size of an array is 1, if an array is empty, there's no way to continue the recursion
        return
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
    
    while left_array_index < len(left_part): # while the left index hasn't got to the last element of the left_part...
        array[sorted_index] = left_part[left_array_index] #... the sorted array will take the remaining elements of the left_part
        sorted_index += 1 # And the sorted_index will be incremented by 1 so the elements can be assigned to it's correct places
    
    while right_array_index < len(right_part): # while the right index hasn't got to the last element of the right_part...
        array[sorted_index] = right_part[right_array_index] #... the sorted array will take the remaining elements of the right_part
        sorted_index += 1 # And the sorted_index will be incremented by 1 so the elements can be assigned to it's correct places
merge_sort([3, 4, 2, 7, 10, 5, 1])