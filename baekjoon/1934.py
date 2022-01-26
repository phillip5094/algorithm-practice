def gcd(a, b):
    if b > a:
        tmp = a
        a = b
        b = tmp

    if a == b:
        return a
    if a % b == 0:
        return b

    return gcd(b, a % b)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))

