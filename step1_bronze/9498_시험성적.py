import sys
input = sys.stdin.readline

# 시험 성적을 input으로 입력 받아 90~100점은 A, 80~89점은 B, 70~79점은 C, 60~69점은 D, 나머지는 F를 출력

score = int(input()) # 성적 입력

if 90 <= score <= 100: # 90~100점이라면
    print("A") # A출력
elif 80 <= score <= 89: # 80~89점이라면
    print("B") # B출력
elif 70 <= score <= 79: # 70~79점이라면
    print("C") # C출력
elif 60 <= score <= 69: # 60~69점이라면
    print("D") # D출력
else: # 나머지는
    print("F") # F출력