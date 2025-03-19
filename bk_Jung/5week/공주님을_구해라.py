'''
그람을 얻은 후부터는 벽을 다 부수고 이동 가능
visited를 2차원으로 만든 후 얻기 전과 얻은 후 구분
'''

N,M,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)]  for _ in range(N)]
print(visited)