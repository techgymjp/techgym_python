print('じゃんけんスタート')
print('自分の手を入力してください')

my_hand = 0
your_hand = 2

if my_hand == 0:
    if your_hand == 0:
        print('あいこ')
    elif your_hand == 1:
        print('勝ち')
    elif your_hand == 2:
        print('負け')
