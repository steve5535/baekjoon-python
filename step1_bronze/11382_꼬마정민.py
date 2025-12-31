import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split()) # 입력받은 값을 공백을 기준으로 나누고 정수로 변환해서 A, B, C에 저장
print(A + B + C) # A + B + C 값을 출력