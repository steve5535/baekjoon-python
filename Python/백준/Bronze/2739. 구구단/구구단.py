import sys
input = sys.stdin.readline

N = int(input()) # 출력할 구구단의 단을 입력받아서 정수로 저장
for i in range(1, 10): # 1부터 9까지 반복
    print(f"{N} * {i} = {N*i}") # N * i = 결과값 형식으로 출력