t = int(input())

for case in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    if even == odd :
        print("YES")
    else :
        print("NO")
