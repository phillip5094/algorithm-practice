str = input()

height = 10

for i in range(1, len(str)):
    if str[i] == str[i -1]:
        height += 5
    else:
        height += 10

print(height)