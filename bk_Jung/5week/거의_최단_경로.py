import heapq

def dijkstra(S):
    pq = []
    heapq.heappush(pq,(0,S))
    distance = [INF] * (N)
    distance[S] = 0 
    

    while pq:
        dist, now= heapq.heappop(pq)  # 가중치와 현재노드
        if distance[now] < dist: # 현재 거리가 더 크면 다음 루트로
            continue
        
        for i in graph[now]:
            cost = dist + i[1] # 다음으로 가는데 드는 비용
            if distance[i[0]] < cost: # 다음으로 가는데 더 크다면 다음으로

                continue
            if distance[i[0]] == cost: # 다음 비용과 같다면 == 최단거리라면
                parents[i[0]].append(now)
                continue
            distance[i[0]] = cost # 다음 가는비용이 더 적다면 초기화
            parents[i[0]] = []
            parents[i[0]].append(now)
            heapq.heappush(pq,(cost,i[0]))
    return distance
def visit_check(D):

    visited[D] = 1
    for i in parents[D]:
        if not visited[i]:
            visit_check(i)
    


def almost_dijkstra(S):
    pq = []
    distance = [INF] * (N)
    heapq.heappush(pq,(0,S))
    distance[S] = 0 


    while pq:
        dist, now= heapq.heappop(pq)  # 가중치와 현재노드
        if distance[now] < dist: # 현재 거리가 더 크면 다음 루트로
            continue

        for i in graph[now]:
            if visited[i[0]]:
                continue
            cost = dist + i[1] # 다음으로 가는데 드는 비용
            if distance[i[0]] < cost: # 다음으로 가는데 더 크다면 다음으로
                continue
            if distance[i[0]] == cost: # 다음 비용과 같다면 == 최단거리라면
                continue
            if straight and now == S and D == i[0]:
                continue
            distance[i[0]] = cost # 다음 가는비용이 더 적다면 초기화
            heapq.heappush(pq,(cost,i[0]))
    return distance



while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0: # 종료 조건건
        break
    S,D = map(int,input().split())
    graph = [[] for _ in range(N)]
    for i in range(M):
        a,b,w = map(int,input().split())
        graph[a].append((b,w)) # 도착지점, 가중치

    INF = 21e9
    distance = [INF] * (N)
 
    parents = [[] for _ in range(N)]
    visited = [0] * N
    init_distance = dijkstra(S)
    visit_check(D)
    straight = False
    if visited[S] and visited[D] and sum(visited) == 2:
        straight = True
    visited[S] = 0
    visited[D] = 0

    almost_dijkstra(S)
    almost_distance = almost_dijkstra(S)
    print(visited)
    print(almost_distance)
    if almost_distance[D] == INF:
        print(-1)
    else:
        print(almost_distance[D])


 