import sys
input = sys.stdin.readline

x = int(input().strip()) # 정수 x를 입력받아 저장
y = int(input().strip()) # 정수 y를 입력받아 저장

if x > 0 and y > 0: # x와 y가 0보다 크면(제1사분면)
    print(1) # 1을 출력
elif x < 0 and y > 0: # x가 0보다 작고 y가 0보다 크면(제2사분면)
    print(2) # 2을 출력
elif x < 0 and y < 0: # x와 y가 0보다 작으면(제3사분면)
    print(3) # 3을 출력
elif x > 0 and y < 0: # x가 0보다 크고 y가 0보다 작으면(제4사분면)
    print(4)