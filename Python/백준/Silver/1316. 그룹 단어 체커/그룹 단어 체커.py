import sys
input = sys.stdin.readline

N = int(input().strip()) # 단어의 개수
count = N # 그룹 단어의 개수

for i in range(N): # 단어의 개수 만큼 반복
    word = input().strip() # 단어를 입력받기
    for j in range(len(word)-1): # 단어의 길이-1 만큼 반복
        if word[j] == word[j+1]: # 지금 문자와 다음 문자가 같으면
            pass # 넘기기
        elif word[j] in word[j+1:]: # 지금 문자가 뒤에 나오면
            count -= 1 # 그룹 단어가 아니여서 그룹 단어의 개수에 -1
            break # 반복문 멈추기

print(count) # 출력