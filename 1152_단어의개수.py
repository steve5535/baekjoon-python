import sys
input = sys.stdin.readline

sentence = input().strip().split() # 입력 받은 문장에 처음과 끝에 공백을 제거하고 공백을 기준으로 단어를 나눈 값을 저장함
sentence_len = len(sentence)

print(sentence_len)