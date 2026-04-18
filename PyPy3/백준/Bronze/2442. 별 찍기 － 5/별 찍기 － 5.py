n = int(input())
for i in range(1, n+1): # n = 5, i = 1
    print((n - i) * " " + i * "*", end="")
    print("*" * (i - 1))