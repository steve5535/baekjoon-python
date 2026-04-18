import sys
input = sys.stdin.readline

N = int(input().strip()) # 정수 N을 입력받는다
long_count = N//4 * "long " # long의 출력 개수를 저장할 변수

print(f"{long_count}int") # 혜야가 생각하는 정수 자료형의 이름을 출력