a, b, c = map(int, input().split())
d = int(input())

sec = (c + d) % 60
rest_min = (c + d) // 60

minute = (b + rest_min) % 60
rest_hour = (b + rest_min) // 60

hour = (a + rest_hour) % 24

print(f'{hour} {minute} {sec}')