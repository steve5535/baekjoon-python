import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split()) # 입력받은 값을 공백으로 나누고 정수로 변황해서 A(시)와B(분)에 저장
C = int(input()) # 요리하는 데 필요한 시간 C를 정수로 저장
B += C # 분에 요리하는데 필요한 시간 더하기
if B >= 60: # B가 60보다 크거나 같으면
    for i in range(B//60):
        B -= 60 # B에 60을 빼고
        A += 1 # A에 1을 더함
if A >= 24: # A가 24보다 크거나 같으면
    A -= 24 # 24를 빼기
print(A, B) # A와B를 공백을 두고 출력