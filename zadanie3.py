with open('my_file.txt', 'r') as file1:
    content = file1.read()

content = content.split()

for i in content:
    print(i)

