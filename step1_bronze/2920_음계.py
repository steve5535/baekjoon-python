import sys
input = sys.stdin.readline

nums = list(map(int, input().strip().split())) # 입력받은 숫자를 리스트에 저장

if nums == sorted(nums): # 입력받은 리스트가 오름차순으로 정렬된 리스트와 같다면
    print("ascending") # ascending를 출력
elif nums == sorted(nums, reverse=True): # 내림차순으로 정렬된 리스트와 같다면
    print("descending") # descending를 출력
else: # 둘다 아니라면
    print("mixed") # mixed를 출력