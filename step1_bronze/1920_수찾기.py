import sys
input = sys.stdin.readline

N = int(input()) # 정수의 개수
N_set = set(map(int, input().split())) # 입력받은 값을 집합에 저장

M = int(input()) # 정수의 개수
M_list = list(map(int, input().split())) # 입력받은 값을 리스트에 저장

for i in M_list: # M_list를 넣어서 반복
    if i in N_set: # N_리스트안에 i가 있다면
        print(1) # 1을 출력
    else: # 아니라면
        print(0) # 0을 출력