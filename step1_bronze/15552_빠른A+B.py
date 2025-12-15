import sys
input = sys.stdin.readline

T = int(input().strip()) # 테스트 케이스 개수
for i in range(T): # T만큼 반복
    A, B = map(int, input().strip().split()) # 입력 받은 값을 공백을 기준으로 나누고 정수로 변환해서 A와B에 저장
    print(A+B) # A와B를 더한 값을 출력