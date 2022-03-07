a_card = list(map(int, input().split(' ')))
b_card = list(map(int, input().split(' ')))

draw_cnt = 0
last_won = None
a_score = 0
b_score = 0
for a, b in zip(a_card, b_card):
    if a == b:
        draw_cnt += 1
        a_score += 1
        b_score += 1
    elif a > b:
        a_score += 3
        last_won = 'a'
    else:
        b_score += 3
        last_won = 'b'
        
print('{0} {1}'.format(a_score, b_score))

if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    if draw_cnt == 10:
        print('D')
    elif last_won == 'a':
        print('A')
    else:
        print('B')