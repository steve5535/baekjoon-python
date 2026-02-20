time = 0
alphabet = input()

for i in range(len(alphabet)):
    if (alphabet[i] in ["A", "B", "C"]):
        time += 3
    elif (alphabet[i] in ["D", "E", "F"]):
        time += 4
    elif (alphabet[i] in ["G", "H", "I"]):
        time += 5
    elif (alphabet[i] in ["J", "K", "L"]):
        time += 6
    elif (alphabet[i] in ["M", "N", "O"]):
        time += 7
    elif (alphabet[i] in ["P", "Q", "R", "S"]):
        time += 8
    elif (alphabet[i] in ["T", "U", "V"]):
        time += 9
    elif (alphabet[i] in ["W", "X", "Y", "Z"]):
        time += 10

print(time)