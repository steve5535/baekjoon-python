import sys
input = sys.stdin.readline

X = int(input().strip()) # 결제된 금액
N = int(input().strip()) # 물건의 종류의 수

sum_price = 0 # 총 가격
for i in range(N): # 물건의 종류의 수 만큼 반복
    a, b = map(int, input().strip().split()) # 물건의 가격 a와 개수 b를 공백을 기준으로 나누고 정수로 변환해서 저장
    sum_price += a * b # 물건의 가격과 개수를 곱한 값을 총 가격에 추가

if X == sum_price: # 결제된 금액과 총 가격이 같다면
    print("Yes") # Yes를 출력
else: # 결제된 금액과 총 가격이 같지 않다면
    print("No") # No를 출력