n = int(input())
plans = list(map(str, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
move_types = ['D', 'U', 'R', 'L']
def travel(x, y):
    for plan in plans:
        for i in range(0, 4):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<1 or nx>n or ny<1 or ny>n:
                    continue
                else:
                    x = nx
                    y = ny
    return x, y #x, y는 지역변수
a, b = travel(1, 1)
print(a, b)