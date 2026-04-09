import sys
input = sys.stdin.readline

word = input().strip().upper() # 입력값 줄바꿈 제거하고 대문자로 변환
count = {} # 나온 문자 갯수 저장 딕셔너리

for i in word:
    if i in count: # 이미 있는 문자라면
        count[i] += 1 # +1
    else: # 아니라면(처음 나왔다면)
        count[i] = 1 # 1로 초기화

max_value = max(count.values()) # 많이 등장한 횟수(딕셔너리에서 밸류가 가장 큰 수) 저장
max_list = [] # 최댓값과 같은 문자를 저장할 리스트

for j in count:
    if count[j] == max_value: # 해당 문자의 밸류가 최댓값과 같으면
        max_list.append(j) # 리스트에 저장

if len(max_list) >= 2: # 최댓값이 여러 개면
    print("?") # ? 출력
else: # 아니라면
    print(max_list[0]) # 가장 많이 나온 문자 출력