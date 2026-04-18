import sys
input = sys.stdin.readline

A, B = input().strip().split() # A와 B를 입력받기
reverse_A = int(A[::-1]) # A를 뒤집어서 정수로 변환
reverse_B = int(B[::-1]) # B를 뒤집어서 정수로 변환

if reverse_A > reverse_B: # 뒤집은 A가 뒤집은 B보다 크면
    print(reverse_A) # 뒤집은 A를 출력
elif reverse_B > reverse_A: # 뒤집은 B가 뒤집은 A보다 크면
    print(reverse_B) # 뒤집은 B를 출력