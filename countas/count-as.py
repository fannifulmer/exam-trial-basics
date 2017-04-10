def count_as(open):
    count_as = open('afile.txt', 'r')
    a_counter = count_as.read()
#try:
    dic = dict()
    for i in count_as:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
#except:
print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
