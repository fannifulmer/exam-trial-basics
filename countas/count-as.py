def count_as(count_as = open('afile.txt', 'r')):
    count_as = open('afile.txt', 'r')
    a_counter = count_as.read()
#try:
counter = 0
for i in range(len(count_as)):
    if count_as[i] == 'a':
        counter += 1
return counter

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0

#except FileNotFoundError:
    #print("0")

