def count_as(count_as):
    try:
        count_as = open('afile.txt', 'r')
        a_counter = count_as.readline()
        a_counter = a_counter.lower()
        return a_counter.count('a')
    except FileNotFoundError:
        print("0")
print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0



