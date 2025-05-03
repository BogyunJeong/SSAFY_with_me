def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

N = int(input())
arr = list(map(int, input().split()))
max_cnt = 0

for i in range(N):
    cnt = 0
    x1 = i + 1
    y1 = arr[i]

    right_slope = -float('inf')
    for j in range(i + 1, N):
        x2 = j + 1
        y2 = arr[j]
        s = slope(x1, y1, x2, y2) 
        if s > right_slope:
            right_slope = s
            cnt += 1

    left_slope = float('inf')
    for j in range(i - 1, -1, -1):
        x2 = j + 1
        y2 = arr[j]
        s = slope(x1, y1, x2, y2)
        if s < left_slope:
            left_slope = s
            cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
