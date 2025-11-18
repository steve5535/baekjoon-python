import sys
input = sys.stdin.readline

# input으로 a와b를 입력받아 split()으로 나누고 a와b를 map을 이용해서 a와b를 정수로 변환
# while문으로 반복
# a와b가 0 이라면 반복 멈춤
# a와b가 0 이 아니라면 a+b값 출력

while True: # 입력 받는 반복문
    a, b = map(int, input().split()) # 숫자 2개를 공백을 이용해서 입력받아 공백으로 나눠서 a와b에 저장
    if a == 0 and b == 0: # a와b가 0이라면
        break # 반복문 멈춤
    print(a+b) # 더한 값 출력