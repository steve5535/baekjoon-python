import sys
input = sys.stdin.readline

c = int(input()) # 테스트 케이스의 개수

for i in range(c): # 테스트 케이스의 개수 만큼 반복
    data = list(map(int, input().split())) # 값을 입력받아서 정수로 변환해 리스트로 저장
    scores = data[1:] # 점수들을 저장한 리스트
    average = sum(scores) / data[0]
    
    count = 0 
    for j in scores:
        if j > average: # 점수가 평균보다 높으면
            count += 1 # +1
    
    proportion = (count / data[0]) * 100 # 비율

    print(f"{proportion:.3f}%") # 소수점 셋째 자리까지 출력