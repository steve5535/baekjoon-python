import sys
input = sys.stdin.readline

T = int(input().strip()) # 테스트 케이스 개수를 입력받는다
for i in range(T): # 테스트 케이스 개수만큼 반복한다
    text = input().strip() # 문자를 입력 받는다
    print(text[0]+text[-1]) # 첫 글자와 마지막 글자를 연속해서 출력