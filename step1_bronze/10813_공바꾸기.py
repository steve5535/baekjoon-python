import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N과M을 입력받는다
basket = list(range(1, N+1)) # N개를 가진 바구니
for i in range(M): # M번 만큼 반복
    i, j = map(int, input().split()) # i와 j를 입력받는다
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1] # i번 바구니와 j번 바구니에 들어있는 공을 교환
print(*basket) # 바구니를 출력