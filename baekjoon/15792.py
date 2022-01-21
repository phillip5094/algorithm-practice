a, b = map(int, input().split())

result = str(a // b) + ''

if a % b:
    result += '.'
    i = 0
    while a % b and i < 1000:
        a = (a % b) * 10
        result += str(a // b)
        i += 1

print(result)