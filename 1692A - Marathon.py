t = int(input())
results = []
for i in range(t):
      distance = list(map(int, input().split()))
      timur_dis = distance[0]
      lst = sorted(distance)
      timur_index = lst.index(timur_dis)
      results.append(4-(timur_index+1))

for result in results:
      print(result)
