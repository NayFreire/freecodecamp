numbers = [3, 1, 5, 34, 56, 10, 9, 5, 2, 4, 7, 8, 12]

even_numbers = lambda even: even % 2 == 0
odd_numbers = lambda odd: odd % 2 != 0

even = list(filter(even_numbers, numbers)) #filter the list numbers with the lambda function
odd = list(filter(odd_numbers, numbers)) #filter(whats supposed to be filtered, filter)

print(even, odd)

