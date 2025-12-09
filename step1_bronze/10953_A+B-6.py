import sys
input = sys.stdin.readline

T = int(input()) # 케이스의 개수
for i in range(T): # 케이스 개수만큼 반복
    A, B = map(int, input().strip().split(",")) # A와 B를 콤마(,)를 기준으로 나누고 정수로 변환해서 저장
    print(A+B) # A와 B를 더한 값을 출력