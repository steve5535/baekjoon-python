import sys
input = sys.stdin.readline

nums = [] # 숫자를 저장할 리스트
for i in range(9): # 9번 반복
    nums.append(int(input())) # 리스트 안에 저장

max = max(nums) # 가장 큰 수 저장

print(max) # 가장 큰수 출력
print(nums.index(max) + 1) # 몇 번째 수인지 출력(가장 큰수의 인덱스번호에 +1 값을 출력)