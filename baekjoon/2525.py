a, b = map(int, input().split())
c = int(input())

hour = (a + (b + c) // 60) % 24
minute = (b + c) % 60
print(f'{hour} {minute}')