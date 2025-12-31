import sys
input = sys.stdin.readline

N = int(input().strip()) # 수의 개수
nums = list(map(int, input().strip().split())) # 입력받은 수를 공백을 기준으로 나누고 정수로 변환해서 리스트에 저장
count = 0 # 소수의 개수

for i in nums: # i에 입력받은 수들을 넣어서 반복
    if i == 1: # 수가 1이라면 (소수가 아니라면)
        continue # i값을 넘기고 반복문으로 돌아가기
    for j in range(2, i): # 2부터 i-1까지를 넣어서 반복
        if i % j == 0: # 나눈나머지 값이 0이면(합성수이면)
            break # 반복을 정지
    else: # 반복을 정지 안했다면(소수 라면)
        count += 1 # 소수 카운트 +1
print(count) # 소수의 개수를 출력