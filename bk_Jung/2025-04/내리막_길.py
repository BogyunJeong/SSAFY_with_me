import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if visited[x][y] != -1: # dp처럼 이미 방문 했으면 탐색 안하고 그 값 전달
        return visited[x][y]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    cnt = 0
    
    visited[x][y] = 0
    # 4방향 탐색
    for k in range(4):

        nx = x + dx[k]
        ny = y + dy[k]

        if -1 < nx < N and -1 < ny < M:
            # 갈 곳이 더 작다면 재귀 시작
            if graph[nx][ny] < graph[x][y]:
                cnt += dfs(nx,ny)

    visited[x][y] = cnt
    return visited[x][y]


N,M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
visited[N-1][M-1] = 1
print(dfs(0,0))


'''
DFS + DP
'''