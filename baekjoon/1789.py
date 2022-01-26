s = int(input())

i = 1

while(True):
    if i * (i + 1) / 2 > s:
        print(i - 1)
        break
    elif i * (i + 1) / 2 == s:
        print(i)
        break
    i += 1
        