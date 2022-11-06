from collections import deque
n, m = map(int, input().split())
graph =[]
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) #2차원 정보는 괄호 안에 넣어서 한번에 append
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 #지나간 자리는 1씩 증가시켜 가며 횟수 카운트
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))