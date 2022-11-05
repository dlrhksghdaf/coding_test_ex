import sys
data = list(map(int, sys.stdin.read().split())) #띄어쓰기 된 모든 인풋을 개별적인 str로 받아들여 리스트화
h = data[0]
w = data[1]
q = data[h*w+2]

mat = []
for i in range (h):
    mat.append(data[2+(w*i): ((i+1)*w)+2])
steps = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for i in range(1, q+1):
    qr_i = data[h*w+3*i] -1
    qc_i = data[h*w+3*i+1] -1
    qv_i = data[h*w+3*i+2]
    k_i = mat[qr_i][qc_i]

    center_candidate = [[qr_i, qc_i]]
    for j in range (0, h*w+5):
        for step in steps:
            n_row = center_candidate[j][0] + step[0]
            n_col = center_candidate[j][1] + step[1]
            if 0<= n_row <=(h-1) and 0<= n_col <=(w-1):
                if mat[n_row][n_col] == k_i:
                    mat[n_row][n_col] = qv_i
                    center_candidate.append([n_row, n_col])
            else:
                continue
        if j == len(center_candidate)-1:
            mat[qr_i][qc_i] = qv_i
            break

for i in range(0, h):
    for j in range(0, w):
        print(mat[i][j], end='\t')
    print()
