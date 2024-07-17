s = list(input())
t = list(input())
new = []

for char in s:
    new.insert(0,char)

if new == t :
    print('YES')
else:
    print('NO')
