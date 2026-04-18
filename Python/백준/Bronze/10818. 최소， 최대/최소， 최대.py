import sys
input = sys.stdin.readline

N = int(input().strip()) # 정수의 개수를 입력 받아서 정수로 변환해 N에 저장
nums = list(map(int, input().strip().split())) # N개의 정수를 입력 받아서 리스트에 저장
nums.sort()
sort_nums = sorted(nums) # 리스트를 오름차순으로 정렬
min = sort_nums[0] # 정렬된 리스트에 1번째 수를 최솟값으로 저장
max = sort_nums[N-1] # 정렬된 리스트에 마지막 수를 최댓값으로 저장

print(min, max) # 최솟값과 최댓값을 공백을 두고 출력