import sys
input = sys.stdin.readline

num_list = list(map(int, input().strip().split())) # 입력받은 값을 공백을 기준으로 나누고 정수로 변환해서 리스트에 저장
num_set = set(num_list) # 리스트를 집합으로 변환

if len(num_set) == 1: # 집합의 길이가 1이라면(수가 모두 같다면)
    print(10000 + (num_list[0] * 1000)) # 1번 상금 출력
elif len(num_set) == 2: # 집합의 길이가 2라면(2수가 같다면)
    print(1000 + (sorted(num_list)[1] * 100)) # 2번 상금 출력
elif len(num_set) == len(num_list): # 집합의 길이와 리스트의 길이가 같다면(수가 모두 다르다면)
    print(max(num_list) * 100) # 3번 상금 출력