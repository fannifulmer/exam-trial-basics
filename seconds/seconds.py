    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]


def seconds(list_of_numbers):
    list_of_numbers = list_of_numbers[1:]
    list_of_number = list_of_numbers[::2]
    return list_of_number
    
print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
