import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N과M을 입력받는다
basket = [0]*N # 바구니에 N만큼 공간을 만든다
for r in range(M): # M만큼 반복한다
    i, j, k = map(int, input().split()) # i, j, k를 입력받는다
    basket[i-1:j] = [k] * (j-i+1) # 바구니에 i부터 j까지 k로 변경
print(*basket) # 바구니를 출력