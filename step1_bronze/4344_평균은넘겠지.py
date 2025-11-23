import sys
input = sys.stdin.readline

c = int(input()) # 테스트 케이스의 개수

for i in range(c): # 테스트 케이스 처리 반복
    data = list(map(int, input().split())) # 한 줄로 입력받아 공백으로 나누고 정수로 변환해서 리스트로 저장
    scores = data[1:] # 첫 번째 값(학생 수)를 제외한 점수들을 리스트로 저장
    average = sum(scores) / data[0] # 평균 값 저장
    
    count = 0 # 평균 보다 점수가 높은 학생 수
    for j in scores:
        if j > average: # 점수가 평균보다 높으면
            count += 1 # 카운트 증가
    
    proportion = (count / data[0]) * 100 # 평균을 넘는 학생의 비율
    print(f"{proportion:.3f}%") # 소수점 셋째 자리까지 출력