arr = [int(input()) for _ in range(9)]
print(f'{max(arr)}\n{arr.index(max(arr)) + 1}')