import sys
input = sys.stdin.readline

num1 = int(input().strip()) # 곱할 1번 숫자 입력(1번 위치)
num2 = input().strip() # 곱할 2번 숫자 입력(2번 위치)

for i in list(num2)[::-1]: # 2번 숫자를 리스트형태로 변환해서 i값에 뒤에서 부터 넣고
    print(num1 * int(i)) # 1번 숫자와 i값을 곱해서 출력(3, 4, 5 위치)

print(num1 * int(num2)) # 곱한 값의 결과 출력(6번 위치)