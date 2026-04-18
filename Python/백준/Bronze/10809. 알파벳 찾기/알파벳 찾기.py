import sys
input = sys.stdin.readline

s = input().strip() # 입력받은 문자열 s
list = [-1] * 26 # 26개 알파벳의 등장 위치 저장 리스트

for idx, ch in enumerate(s): # idx에 현재 문자 인덱스추가 ch에 현재 문자 추가
    pos = ord(ch) - ord("a") # 현재 문자가 알파벳에서 몇 번째인지 확인
    if list[pos] == -1: # 해당 문자가 처음 등장했으면
        list[pos] = idx # 그 위치(인덱스)를 저장

print(*list) # 공백으로 구분해서 출력