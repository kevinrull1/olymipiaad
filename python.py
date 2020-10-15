names = open('names.txt', 'r')
firstline = names.readline()
l = firstline.split()
for i in range(3):
    print(names.readline())
