import sys
input = sys.stdin.readline

A = int(input().strip()) # A를 정수로 입력 받는다
B = int(input().strip()) # B를 정수로 입력 받는다
C = int(input().strip()) # C를 정수로 입력 받는다
list = [0]*10 # 0이 10개 들어있는 리스트를 생성

ABC = A*B*C # AxBxC 값을 저징
for i in str(ABC): # AxBxC값을 넣어서 반복
    list[int(i)] += 1 # 리스트에 인덱스 번호 i값에 +1
print(*list, sep="\n") # 리스트에 요소를 줄마다 출력