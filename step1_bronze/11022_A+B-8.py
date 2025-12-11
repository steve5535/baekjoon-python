import sys
input = sys.stdin.readline

T = int(input()) # 케이스 개수
for i in range(T): # 케이스 개수 만큼 반복
    A, B = map(int, input().strip().split()) # A와B를 입력받은 값을 공백을 기준으로 나누고 정수로 변환해서 저장
    C = A+B # C값을 A+B로 저장
    x = i+1 # 테스트 케이스 번호
    print(f"Case #{x}: {A} + {B} = {C}") # "Case #x: A + B = C" 형식으로 출력