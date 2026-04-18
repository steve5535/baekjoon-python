N = int(input())
list = list(map(int, input().strip().split()))
sort_list = sorted(list)
if len(list) != len(set(list)):
    print(0)
elif list == sort_list:
    print(1)
else:
    print(0)