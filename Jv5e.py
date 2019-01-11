import random

hands = ['グー', 'チョキ', 'パー']
results = {'win':'勝ち', 'lose':'負け', 'draw':'あいこ'}

def start_message():
  print('じゃんけんスタート')

def get_my_hand():
  print('自分の手を入力してください')
  input_message = ''
  index = 0
  for hand in hands:
    input_message += str(index) + ':' + hand
    if index < 2:
      input_message += ', '
    index += 1
  return int(input(input_message))

def get_you_hand():
  return random.randint(0, 2)

def get_hand_name(hand_number):
  return hands[hand_number]

def view_hand(my_hand, you_hand):
  print('自分の手は ' + get_hand_name(my_hand))
  print('相手の手は ' + get_hand_name(you_hand))

def get_result(hand_diff):
  if hand_diff == 0:
    return 'draw'
  elif hand_diff == -1 or hand_diff == 2:
    return 'win'
  else:
    return 'lose'

def view_result(result):
  print(results[result])


start_message()

my_hand = get_my_hand()
you_hand = get_you_hand()
hand_diff = my_hand - you_hand

view_hand(my_hand, you_hand)
result = get_result(hand_diff)
view_result(result)
