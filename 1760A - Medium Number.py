n = int(input())

for i in range (n):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    print(lst[1])
