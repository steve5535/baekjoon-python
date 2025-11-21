import sys
input = sys.stdin.readline

# 세 수를 imput으로 입력받아 리스트에 저장해 오름차순으로 정렬해서 출력한다

nums = list(map(int, input().split())) # 숫자를 입력받아 리스트 안에 저장
nums.sort() # 오름차순으로 정렬

print(*nums) # 리스트 출력