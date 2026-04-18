word = input() # 단어를 입력받는다
revers_word = word[::-1] # 입력받은 단어를 뒤집기

if word == revers_word: # 단어랑 입력받은 단어랑 같은지 확인
    print(1) # 같다면 1을 출력
else: # 다르다면
    print(0) # 0을 출력