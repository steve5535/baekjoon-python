import sys
input = sys.stdin.readline

count = [0]*10001 # 값을 저장할 리스트
num = int(input()) # 정렬할 숫자 개수

for i in range(num):
    x = int(input())
    count[x] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        sys.stdout.write(str(i) + "\n")