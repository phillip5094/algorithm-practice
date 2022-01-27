case1 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

case2 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

def calculateRedrawCount(start_x, start_y):
    case1_count = 0
    case2_count = 0
    for i in range(8):
        for j in range(8):
            if case1[i][j] != arr[start_x + i][start_y + j]:
                case1_count += 1
            if case2[i][j] != arr[start_x + i][start_y + j]:
                case2_count += 1
    return min(case1_count, case2_count)


n, m = map(int, input().split())
arr = []
redraw_count = 65

for i in range(n):
    arr.append(input())


for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        redraw_count = min(redraw_count, calculateRedrawCount(i, j))

print(redraw_count)