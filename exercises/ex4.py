file = open("bear.txt", "r")

content = file.readlines()

for row in content:
    print(row)
