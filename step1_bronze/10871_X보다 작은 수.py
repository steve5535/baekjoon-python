import sys
input = sys.stdin.readline

N, X = map(int, input().split()) # N = 수열 개수, X = 정수
A = list(map(int, input().split())) # 입력받은 수열을 공백으로 나눠서 정수로 변환해서 리스트형태로 저장

small_num = [] # X보다 작은수 추가할 리스트
for i in range(N): # 수열 개수 만큼 반복
    if A[i] < X: # 리스트A에 인덱스 번호 i인 수가 X보다 작으면
        small_num.append(A[i]) # small_num리스트에 추가

print(*small_num) # small_num 출력