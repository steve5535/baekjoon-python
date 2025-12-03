import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수

for i in range(T): # 케이스 만큼 반복
    R, S = input().strip().split() # R에는 반복횟수 저장, S에는 문자열 저장
    P = "" # 반복한 문자를 저장할 변수
    for j in range(len(S)): # 문자열의 길이만큼 반복
        P += int(R) * S[j] # P변수에 정수로 변환한 반복횟수와 문자열에 인덱스 번호가 j인 문자를 곱한 값을 저장
        
    print(P) # 출력