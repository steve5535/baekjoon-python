import sys
input = sys.stdin.readline

# input으로 a와b를 입력받아 split(" ")으로 나누고 a와b를 int()로 정수로 변환
# while문으로 반복
# a와b가 0 이라면 반복 멈춤
# for문으로 더한 값들을 한줄식 출력

add = [] # 더한값을 저장할 리스트
while True: # 입력 받는 반복문
    a, b = (input()).split(" ") # 숫자 2개를 공백을 이용해서 입력받아 공백으로 나눠서 a와b에 저장
    a = int(a) # a를 정수로 변환
    b = int(b) # b를 정수로 변환
    add.append(a+b) # a와b를 더한 값을 add리스트에 추가
    if a == 0 and b == 0: # a와b가 0이라면
        add.remove(0) # 마지막 0 0은 제거
        break # 반복문 멈춤

for i in add: # for 문으로
    print(i) # add리스트 안에 있는 값들을 한줄식 출력