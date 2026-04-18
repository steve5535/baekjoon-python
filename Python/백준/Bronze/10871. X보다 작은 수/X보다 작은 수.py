import sys
input = sys.stdin.readline

N, X = map(int, input().split()) 
A = list(map(int, input().split())) 

small_num = [] 
for i in range(N): 
    if A[i] < X: 
        small_num.append(A[i]) 

print(*small_num) 