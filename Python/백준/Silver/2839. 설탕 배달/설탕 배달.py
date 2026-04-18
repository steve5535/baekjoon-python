import sys
input = sys.stdin.readline

N = int(input()) # 배달해야하는 킬로그램

five = N // 5 # 5로 나눌 횟수
answer = -1 # 답을 저장할 변수

while five >= 0: # 횟수가 0보다 크면
    rest = N - five * 5 # 나머지
    if rest % 3 == 0: # 나머지를 3으로 나눈몫이 0이라면
        answer = five + (rest // 3) # 답을 5로 나눌 횟수 + 나머지를 3으로 나눈몫으로 저장
        break
    five -= 1 # 반복할 횟수 줄이기

print(answer) # 답 출력