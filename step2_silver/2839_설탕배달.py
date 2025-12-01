import sys
input = sys.stdin.readline

N = int(input()) # 배달해야하는 킬로그램

five = N // 5 # 5kg 봉지로 얼마나 쓸 수 있는지 확인하는 변수
answer = -1 # 답을 저장할 변수

while five >= 0: # 5kg 봉지 개수가 0이상인 동안 반복
    rest = N - five * 5 # 5kg 봉지를 쓴 다음에 설탕 무게(나머지)
    if rest % 3 == 0: # 나머지가 3으로 나누어 떨어지면
        answer = five + (rest // 3) # 답을 5kg 봉지를 사용한 횟수 + 나머지를 3으로 나눈몫으로 저장
        break
    five -= 1 # 5kg 봉지 개수를 하나 줄이기

print(answer) # 답 출력