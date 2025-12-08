import sys
input = sys.stdin.readline

while True: # 무한 반복 한다
    try: # 시도해본다
        A, B = map(int, input().strip().split()) # A와 B를 공백을 기준으로 나눠서 정수로 저장
    except ValueError: # 벨류에러가 뜨면
        break # 반복 정지
    else:
        print(A+B) # A와 B를 더한 값을 출력