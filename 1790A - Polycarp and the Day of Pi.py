i = int(input())
pi = "314159265358979323846264338327"

for _ in range(i):
    n = input()
    count = 0
    for i in range(len(n)):
        if n[i] == pi[i]:
            count +=1
            continue
        else:
            break

    print(count)
