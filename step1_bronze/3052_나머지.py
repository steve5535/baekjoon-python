import sys
input = sys.stdin.readline

nums = [] # 리스트 생성
for i in range(10): # 10번 반복
    num = int(input()) # 입력받은 값을 정수로 변환해서 저장
    nums.append(num%42) # 수를 42로 나눈값에 나머지를 리스트에 저장
print(len(set(nums))) # 리스트를 집합으로 변환한뒤 집합의 길이를 출력