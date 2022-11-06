from collections import deque
n, m = map(int, input().split())
graph =[]
for _ in range(n):
    graph.append(list(map(int, input())))
def bfs(x, y, visited):
    queue = deque([x, y]) #좌표
    visited[x][y] = True #방문여부
    while queue:
        global count
        matrix = []
        v_x = queue.popleft() #좌표하나 변수 할당
        v_y = queue.popleft()
        if 0 <= v_x+1 <n:
            matrix = [[v_x+1, v_y]]
        if 0 <= v_x-1 <n:
            matrix.append([v_x-1, v_y])
        if 0 <= v_y+1 < n:
            matrix.append([v_x, v_y+1])
        if 0 <= v_y-1 < n:
            matrix.append([v_x, v_y-1])
        print(matrix)
        for i in matrix: #입력된 matrix의 특정 좌표의 값을 체크하는 것
            if not visited[i[0]][i[1]]:
                queue.append(i[0])
                queue.append(i[1])
                print(queue)
                visited[i[0]][i[1]] = True
                count += 1
            if i[0]+i[1] == n+m-2:
                print(count)
                return

visited =[]
visited2 = []
count = 0
for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == 0:
            visited.append(True)
        else:
            visited.append(False)
for i in range(0, n):
        visited2 = visited2 + [visited[0:m]]
        del visited[0:m]

bfs(0, 0, visited2)