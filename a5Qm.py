import random

print('じゃんけんスタート')

print('自分の手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0, 2)

hand_diff = my_hand - you_hand

if hand_diff == 0:
  print('あいこ')
elif hand_diff == -1 or hand_diff == 2:
  print('勝ち')
else:
  print('負け')
