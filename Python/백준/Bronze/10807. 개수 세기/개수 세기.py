import sys
input = sys.stdin.readline

N = int(input().strip()) # 정수의 개수를 입력받을 변수
nums = list(map(int, input().strip().split())) # 입력받은 수를 공백을 기준으로 나누고 정수로 변환해서 리스트에 저장
V = int(input().strip()) # 찾으려고 하는 정수를 입력받을 변수
count = 0 # 찾으려는 정수의 개수를 저장할 변수

for i in nums: # i에 입력받은 정수들을 넣어서 반복
    if i == V: # 입력받은 정수가 찾으려는 정수와 같다면
        count += 1 # 정수의 개수를 저장한 변수에 +1

print(count) # 정수의 개수를 저장한 변수를 출력