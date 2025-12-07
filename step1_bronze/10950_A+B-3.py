import sys
input = sys.stdin.readline

T = int(input()) # 케이스 개수
for i in range(T): # T만큼 반복
    A, B = map(int, input().strip().split()) # A와B를 공백을 기준으로 나눠서 정수로 변환해서 저장
    print(A+B) # A와B를 더한 값을 출력