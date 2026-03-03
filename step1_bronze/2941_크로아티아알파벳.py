alphabet = input() # 입력을 받는다
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 크로아티아 알파벳 저장

for i in croatia: # i에 크로아티아 알파벳을 넣어서 반복한다
    alphabet = alphabet.replace(i, "*") # i(크로아티아 알파벳)을 *로 바꾼다
print(len(alphabet)) # 문자의 길이를 확인한다