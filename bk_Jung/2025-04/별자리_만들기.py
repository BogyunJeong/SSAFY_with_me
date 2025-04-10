import math
import heapq


def prim(start):
    visited[start] = 1
    p = list(graph[start])
    heapq.heapify(p)
    res = 0

    while p:
        dist, now = heapq.heappop(p)
        
        if visited[now]:
            continue
        res += dist
        visited[now] = 1
        for edge in graph[now]:
            if not visited[edge[1]]:
                heapq.heappush(p,(edge))

    return res

n = int(input())

coordinate = []
graph = [[] for _ in range(n)]

for i in range(n):
    x,y = map(float,input().split())
    coordinate.append((x,y))

for i in range(n):
    x1,y1 = coordinate[i]
    for j in range(n):
        if i == j:
            continue
        x2,y2 = coordinate[j]

        d = math.sqrt(((x1 - x2) **2) + ((y1 - y2) ** 2)) # 현재에서 다른 좌표까지의 거리
        graph[i].append((d,j)) # 거리와 그 지점 숫자를 넣음

visited = [0] * n

result = prim(0)
print(f'{result:.2f}')