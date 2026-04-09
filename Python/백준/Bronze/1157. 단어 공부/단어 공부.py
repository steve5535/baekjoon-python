word = list(input().upper()) # 입력받은 단어를 대문자로 변환하고 리스트 형태로 저장
dic = {} # 딕셔너리 생성

for i in set(word): # 단어에 들어있는 알파벳을 넣어서 반복
    dic[i] = word.count(i) # 딕셔너리에 key에는 i값(알파벳)을 value에는 사용된 알파벳의 개수로 저장

counts = list(dic.values()) # 딕셔너리에 저장된 value들(사용된 알파벳 개수)을 리스트형태로 저장
max_count = max(counts) # 리스트에서 가장 큰값(가장 많이 사용된 알파벳 개수)을 저장

if counts.count(max_count) > 1: # 리스트에 있는 값중에 가장큰 값이 1개 이상이면
    print("?") # "?"를 출력
else: # 아니라면
    print(max(dic, key=dic.get)) # value가 가장 큰 값을 출력