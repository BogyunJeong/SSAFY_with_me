import heapq
import math

N,M = map(int,input().split()) # 노드수, 간선 수

coodinate = []
for i in range(N):
    x,y = map(int,input().split())
    coodinate.append((x,y))

graph = [[] for _ in range(N+1)]
print(coodinate)
for i in range(N):
    x1,y1 = coodinate[i]
    for j in range(N):
        if i == j:
            continue
        x2,y2 = coodinate[j]
        d = math.sqrt(((x1-x2)**2) + (y1-y2)**2)
        graph[i].append(d)

print(graph)