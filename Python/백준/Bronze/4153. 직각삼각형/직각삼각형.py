import sys
input = sys.stdin.readline

while True: # 무한 반복
    side = list(map(int, input().strip().split())) # 입력받은 값을 공백을 기준으로 나누고 정수로 변환해서 리스트에 저장
    if side == [0, 0, 0]: # 입력값이 0 0 0 이면
        break # 정지
    max_side = max(side) # 빗변을 저장
    side.remove(max_side) # 변들이 저장되있는 리스트에서 빗변을 제거
    if max_side**2 == side[0]**2 + side[1]**2: # 피타고라스 정리가 성립한다면
        print("right") # right를 출력
    else: # 성립하지 않다면
        print("wrong") # wrong를 출력