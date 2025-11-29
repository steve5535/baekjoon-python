import sys
input = sys.stdin.readline

num = int(input()) # 시험 개수
test_scores = list(map(int, input().split())) # 시험 점수들
test_max = max(test_scores) # 시험 점수 중 가장 높은 점수

change_scores = [] # 바뀐 점수를 저장할 리스트
for i in range(num):
    change_scores.append(test_scores[i] / test_max * 100) # 점수 ÷ 가장 높은 점수 × 100

average = sum(change_scores) / num # 바뀐 점수들의 평균
print(average) # 평균 출력