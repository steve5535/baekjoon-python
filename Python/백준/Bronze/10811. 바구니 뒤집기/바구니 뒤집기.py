import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N과 M을 입력받는다
basket = [x+1 for x in range(N)] # 1부터 N까지 리스트에 추가
for y in range(M): # M번 만큼 반복한다
    i, j = map(int, input().split()) # i와 j를 입력받는다
    temp = basket[i-1:j] # i부터 j까지 값을 불러온다
    temp.reverse() # 불러온 값을 뒤집는다
    basket[i-1:j] = temp # 뒤집은 값을 리스트에 추가한다
print(*basket) # 리스트를 출력한다