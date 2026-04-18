import sys
input = sys.stdin.readline

count = int(input()) # 숫자 몇개 받을지 저장하는 변수
nums = [] # 숫자들을 저장할 리스트

for i in range(count):
    nums.append(int(input())) # 입력받은 값을 정수로 변환해서 리스트에 저장

nums.sort() # 오름차순으로 정렬
print(*nums, sep="\n") # sep구분자를 이용해서 공백을 줄바꿈으로 변환해서 한줄씩 출력