import sys
input = sys.stdin.readline

# input 으로 연도를 입력받고 if 문으로 윤년인지 아닌지 판별

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # (4의 배수이면서 100의 배수가 아닐 때) 또는 (400의 배수일때)
    print(1) # 1을 출력
else: # 아니라면
    print(0) # 0을 출력