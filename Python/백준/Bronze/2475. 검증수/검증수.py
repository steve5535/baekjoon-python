import sys
input = sys.stdin.readline

unique_number = list(map(int, input().strip().split())) # 입력 받은 고유번호를 공백을 기준으로 나누고 정수로 변환해서 리스트로 저장
square_number = [i**2 for i in unique_number] # 고유번호를 각각 제곱한 수를 리스트로 저장
print(sum(square_number) % 10) # 검증수(고유번호를 각각 제곱한 수들의 합을 10으로 나눈 나머지)를 출력