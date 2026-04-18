pis = [1, 1, 2, 2, 2, 8]
need_pis = []

input_pis = list(map(int, input().split()))
for i in range(0, 6):
    need_pis.append(pis[i] - input_pis[i])
print(*need_pis)

# 있던값 - 입력받은값