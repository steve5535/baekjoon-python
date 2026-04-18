import sys
input = sys.stdin.readline

word = set() # 단어들을 추가할 집합을 만든다
N = int(input().strip()) # 단어의 개수 N
for i in range(N): # N번 만큼 반복한다
    word.add(input().strip()) # 단어를 입력받아서 집합에 추가해서 중복을 제거한다

sorted_word = sorted(list(word)) # 집합을 리스트로 변경하고 사전 순으로 정렬한다
sorted_word.sort(key=len) # 단어의 길이를 순으로 정렬한다

print(*sorted_word, sep="\n") # 리스트의 값을 줄별로 출력한다