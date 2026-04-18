import sys
input = sys.stdin.readline

S = input().strip() # 단어를 입력 받아서 S에 저장
i = int(input().strip()) # 입력 받은 값을 정수로 변환해서 i에 저장
print(S[i-1]) # S의 i-1 인덱스 값을 출력