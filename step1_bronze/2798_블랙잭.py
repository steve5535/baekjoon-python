import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N과 M을 입력 받는다
card = list(map(int, input().split())) # N개 입력받은 리스트에 저장한다
max_sum = 0 # 최대한 가까운 합을 저장할 변수

for i in range(0, N-2): # 0부터 N-2(마지막에 카드 2장을 남기고)까지 반복을 한다
    for j in range(i+1, N-1): # 0부터 N-1(마지막에 카드 1장을 남기고)까지 반복을 한다
        for k in range(j+1, N): # 0부터 N까지 반복을 한다
            current_sum = card[i] + card[j] + card[k] # 3장의 카드의 합을 변수에 저장한다
            if current_sum == M: # 저장한 변수가 M과 같다면
                max_sum = current_sum # 현재까지의 최대 합을 업데이트 한다
                print(max_sum) # 출력하고
                sys.exit() # 반복문을 멈춘다
            elif current_sum < M and current_sum > max_sum: # 3장의 카드를 저장한 값이 M보다 작고 M과 최대한 가까운 수보다 크다면
                max_sum = current_sum # 현재까지의 최대 합을 업데이트 한다
                
print(max_sum) # M과 최대한 가까운 합을 출력한다