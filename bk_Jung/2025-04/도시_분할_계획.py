import heapq


def prim(start): # 프림 알고리즘 시작
    p = list(graph[start])
    heapq.heapify(p)
    res = []
    max_path = 0
    visited[start] = 1
    while p:
        dist, now = heapq.heappop(p)

        if visited[now]:
            continue

        visited[now] = 1
        res.append(dist)
        max_path = max(max_path,dist)
        for edge in graph[now]:
            if not visited[edge[1]]:
                heapq.heappush(p,(edge))

    return sum(res) - max_path

N,M = map(int,input().split()) # 노드 수, 간선 수
graph = [[] for _ in range(N+1)]


for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

visited = [0] * (N+1)
result = prim(1)

print(result)