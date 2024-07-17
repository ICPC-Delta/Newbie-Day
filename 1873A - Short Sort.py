def check(cards):
    if (cards == 'abc') or (cards[0] == 'a') or (cards[1] == 'b') or (cards[2] == 'c'):
        return "Yes"
    else:
        return "No"

t = int(input())
for case in range(t):
    cards = input()
    print(check(cards))
        
