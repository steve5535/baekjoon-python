import sys
input = sys.stdin.readline

H, M = map(int, input().strip().split()) # 시간을 공백을 기준으로 나누고 정수로 변환해서 H와M에 저장
M -= 45 # 분에 45를 빼기
if M < 0: # 만약 분이 0보다 작다면
    H -= 1 # 시간에 1빼고
    M += 60 # 분에 60을 더한다
if H < 0: # 시간이 0보다 작다면
    H += 24 # 시간에 24를 더한다
print(H, M) # 시간과 분을 출력한다