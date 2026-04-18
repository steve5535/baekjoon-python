import sys
input = sys.stdin.readline

count = int(input()) # 더할 숫자 개수 입력 받는 변수
num = input().strip() # 문자열로 숫자 입력 받는 변수

num_list = [] # 숫자들을 나눠서 저장할 리스트
for i in range(count):
    num_list.append(int(num[i])) # 문자열을 정수로 변환해서 리스트에 저장

sum_num = sum(num_list) # 리스트에 숫자들을 더한 변수
print(sum_num) # 합 출력