import sys
input = sys.stdin.readline

N = int(input()) # 학과의 수를 정수로 저장
department_dic = {} # 학과 이름과 연도를 저장할 딕셔너리
for i in range(N): # N만큼 반복
    name, year = input().strip().split() # 입력 받은 값을 공백을 기준으로 나누고 이름과 연도에 저장
    department_dic[name] = int(year) # 이름을 벨류, 연도를 키로 딕셔너리에 저장

for key, value in department_dic.items():
    if value == 2026:
        print(key)