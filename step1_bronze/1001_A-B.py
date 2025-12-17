import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split()) # 입력 받은 값을 공백으로 나누고 정수로 전환해서 A와B에 저장
print(A-B) # A-B값을 출력