import sys
input = sys.stdin.readline

case = int(input().strip()) # 케이스 개수

for i in range(case): # 케이스 개수 만큼 반복
    final_score = 0 # 최종 점수
    add_score = 0 # 추가 점수
    result = input().strip() # OX 결과값
    for j in result: # OX 결과값을 넣어서 반복
        if j == "O": # OX 결과값이 O라면
            add_score += 1 # 추가 점수 +1
            final_score += add_score # 최종 점수에 추가점수 추가
        else: # 아니라면
            add_score = 0 # 추가 점수 0
    print(final_score) # 최종 점수 출력