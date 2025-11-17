import sys
input = sys.stdin.readline

num = int(input()) # 입력할 숫자 개수
nums = [] # 입력한 숫자 추가할 리스트

for i in range(num):
    nums.append(int(input()))

nums.sort() # 오름차순으로 정렬

for j in nums:
    print(j)