    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

def seconds(list_of_numbers = []):
    for i in range(len(list_of_numbers)+1):
        if list_of_numbers[i] % 2 == 0:
            list_of_numbers.remove(list_of_numbers[i])
            i += 1
            
print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]

'''list_of_numbers = [1, 2, 3, 4, 5]
numbers = []
for i in range(len(list_of_numbers)):
if list_of_numbers[i] % 2 == 0:
    numbers.append(list_of_numbers[i])
    i += 1
print(numbers)'''