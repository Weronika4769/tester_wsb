with open('tracert-result.txt', 'r') as f:
    lines = f.readlines()

count = 0
for i in range(4, len(lines)-2):
    count +=1
    line = lines[i]
    line = line.split()
    print(line[-1])

print(count)
