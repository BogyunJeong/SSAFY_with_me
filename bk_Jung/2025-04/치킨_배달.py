def chick_dilivery(perm):
    total = 0
    for x1,y1 in h:
        dist = 21e9
        for x2,y2 in perm:
            dist = min(dist,abs(x1-x2)+abs(y1-y2))
        total += dist
    return total
def permutation(idx,cnt):
    global min_result
    if cnt == M:
        s = perm[:M]
        dist = chick_dilivery(s)
        min_result = min(min_result,dist)
        return
    if idx == len(c):
        return

    perm[cnt] = c[idx]
    permutation(idx + 1,cnt+1)

    permutation(idx +1,cnt)

'''
치킨집을 순열로 M개 뽑음
뽑은 치킨집에서 치킨 거리의 최소값 구해봄
만약 구하다가 더 크면 가지치기 하기
'''

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
c = [] #치킨집 위치 담을 변수
h = [] # 집 위치 담을 변수
perm = [0] * M # 순열 담을 변수
min_result = 21e9
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            h.append((i,j))
        elif graph[i][j] == 2:
            c.append((i,j))

used = [0] * len(c)
result = [0] * len(h)
cnt = 0
permutation(0,0)

print(min_result)
