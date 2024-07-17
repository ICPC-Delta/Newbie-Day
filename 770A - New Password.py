target_len, distinct_chars = map(lambda x: int(x), input().split())

letters = 'abcdefghijklmnopqrstuvwxyz'
password = ""

while len(password) < target_len:    
    for i in range(distinct_chars):
        if len(password) < target_len:
            password += letters[i]
        else:
            break

print(password)
