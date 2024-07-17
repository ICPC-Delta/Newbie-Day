n = int(input())
results = []

for i in range (n):
    length = int(input())
    case = input()

    if sorted(case) == sorted("miurT"):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)
