import sys
input = sys.stdin.readline

A, B = map(int, input().split()) # A와 B값을 받아서 정수로 저장

if A > B: # A가 B보다 크면
    print(">") # '>'출력
elif A < B: # A가 B보다 작으면
    print("<") # '<'출력
elif A == B: # A와 B가 같으면
    print("==") # '=='출력