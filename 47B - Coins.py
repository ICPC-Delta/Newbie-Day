lst = []
dic={
    "A":0,
    "B":0,
    "C":0
}


for _ in range(3):
    lst.append(input())
    
for sub_list in lst:
    if ">" in sub_list:
        dic[sub_list[0]]+=1
    else:
        dic[sub_list[2]]+=1
        
if len(set(list(dic.values()))) != 3:
    print("Impossible")'
else:
    sorted_keys = [k for k, v in sorted(dic.items(), key=lambda item: item[1])]
    print("".join(sorted_keys))
