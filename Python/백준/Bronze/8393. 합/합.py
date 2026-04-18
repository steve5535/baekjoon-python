import sys
input = sys.stdin.readline

def add_num(n): # 1부터 n까지 합을 구하는 함수
    for i in range(n): # n만큼 반복
        n+=i # n에 반복 순서를 더함
    print(n) # n을 출력

n = int(input()) # n을 정수로 입력받기
add_num(n) # n을 인수로 하고 함수를 호출