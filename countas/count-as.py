def count_as(count_number):
    try:
        count_number = open(count_number, 'r')
        a_counter = count_number.readline()
        a_counter = a_counter.lower()
        return a_counter.count('a')
    
    except FileNotFoundError:
        return 0
print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0



