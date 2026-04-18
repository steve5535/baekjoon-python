import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수(정수)
for i in range(T): # 테스트 케이스 만큼 반복
    A, B = map(int, input().strip().split()) # 공백을 기준으로 나누고 정수로 변환해서 A와B로 저장
    print(f"Case #{i+1}: {A+B}") # x를 테스트 반복 횟수로 두고"Case #x: A+B"값을 출력