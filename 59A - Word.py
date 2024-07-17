s = input()
upper_counter = 0
lower_counter = 0

for i in range(len(s)):
      if s[i].isupper():
            upper_counter +=1
      elif s[i].islower():
            lower_counter +=1

if upper_counter > lower_counter:
      print(s.upper())

else:
      print(s.lower())
