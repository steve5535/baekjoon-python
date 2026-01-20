import sys
input = sys.stdin.readline

matrix_A = [] # 행렬 A를 저장할 리스트
matrix_B = [] # 행렬 B를 저장할 리스트
N, M = map(int, input().split()) # N과 M을 입력받는다
for i in range(N): # N(행)만큼 반복한다
    row_a = list(map(int, input().split())) # 행의 값을 입력받아서 리스트에 정수로 저장한다
    matrix_A.append(row_a) # 행렬 A에 행을 추가한다
for j in range(N): # N(행)만큼 반복한다
    row_b = list(map(int, input().split())) # 행의 값을 입력받아서 리스트에 정수로 저장한다
    matrix_B.append(row_b) # 행렬 A에 행을 추가한다

for x in range(N): # N(행)만큼 반복
    row = [] # 행을 더한 값을 저장할 리스트
    for y in range(M): # M(열)만큼 반복
        entry = matrix_A[x][y] + matrix_B[x][y] # 성분변수에 A행렬과 B행렬에 성분을 더한 값을 추가
        row.append(entry) # 더한 요소을 행리스트에 저장
    print(*row) # 리스트에 저장한 값을 출력