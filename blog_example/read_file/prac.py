f = open("test.txt", 'r')
line = f.readlines()
for i in range(len(line)):
    if (line[i][-1] == '\n'):
        line[i] = line[i][:-1]
print(line)