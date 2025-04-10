import heapq
import sys


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



N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
max_result = 0
for i in range(M):
    a,b,w = map(int,sys.stdin.readline().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
    max_result += w
visited = [0] * (N+1)

result = prim(1)

if sum(visited) == N:    
    print(max_result - result)
else:
    print(-1)
