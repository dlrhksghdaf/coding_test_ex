n, m = map(int, input().split()) #띄어쓰기 된 모든 인풋을 개별적인 str로 받아들여 리스트화
matrix = []
tmp_graph =[]
steps = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for _ in range(n):
    matrix.append(list(map(int, input())))

def find_num_icecream(graph, x, y):
    tmp_graph = []
    global count
    graph[x][y] = 1
    center_candidate = [[x, y]]
    for j in range (0, n*m):
        for step in steps:
            n_row = center_candidate[j][0] + step[0]
            n_col = center_candidate[j][1] + step[1]
            if 0<= n_row <=(n-1) and 0<= n_col <=(m-1):
                if graph[n_row][n_col] == 0:
                    graph[n_row][n_col] = 1
                    center_candidate.append([n_row, n_col])
            else:
                continue
        if j == len(center_candidate)-1:
            # print(graph)
            for i in graph:
                tmp_graph.extend(i)
            # print(sum(tmp_graph))
            if sum(tmp_graph) < n*m:
                tmp_loc = tmp_graph.index(0)
                count +=1
                find_num_icecream(graph, tmp_loc // m, tmp_loc % m)
            return

for i in matrix:
    tmp_graph.extend(i)
loc = tmp_graph.index(0)
if sum(tmp_graph) == n*m:
    count = 0
else:
    count = 1
find_num_icecream(matrix, loc//m, loc%m)
print(count)