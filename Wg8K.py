import random
import math

teams = []
playing_teams = {'myself': False, 'enemy': False}

class Team:
  def __init__(self, id, name, attack, defense):
    self.id = id
    self.name = name
    self.attack = attack
    self.defense = defense
    self.total_score = 0

  def info(self):
    print(self.name + ': 攻撃力:' + str(self.attack) + ' / 守備力:' + str(self.defense))

  def get_hit_rate(self):
    return random.randint(10, self.attack)

  def get_out_rate(self):
    return random.randint(10, self.defense)

def create_teams():
  global teams
  team1 = Team(1, 'アタッカーズ', 80, 20)
  team2 = Team(2, 'ディフェンダーズ', 30, 70)
  team3 = Team(3, 'アベレージーズ', 50, 50)
  teams = [team1, team2, team3]

def show_teams():
  index = 1
  print('全チームの情報')
  for team in teams:
    print(str(index))
    team.info()
    index += 1

def choice_team(player):
  if player == 'myself':
    player_name = '自分'
  elif player == 'enemy':
    player_name = '相手'

  choice_team_message = player_name + 'のチームを選択してください（1〜3）'
  choice_team_number = input(choice_team_message)
  while not enable_choice_team(choice_team_number, player):
    choice_team_number = input(choice_team_message)
  choice_team_number = int(choice_team_number)

  playing_teams[player] = teams[choice_team_number - 1]
  print(player_name + 'のチームは「' + playing_teams[player].name + '」です')

def enable_choice_team(string, player):
  if string.isdigit():
    number = int(string)
    if number >= 1 and number <= 3:
      if player == 'enemy':
        if number == playing_teams['myself'].id:
          return False
      return True
    else:
      return False
  else:
    return False

def get_play_inning(inning):
  if inning == 'front':
    hit_rate = playing_teams['myself'].get_hit_rate()
    out_rate = playing_teams['enemy'].get_out_rate()
  elif inning == 'back':
    hit_rate = playing_teams['enemy'].get_hit_rate()
    out_rate = playing_teams['myself'].get_out_rate()
  inning_score = math.floor((hit_rate - out_rate) / 10)
  if inning_score < 0:
    inning_score = 0
  return inning_score

def get_special_inning():
  special_number = random.randint(1, 5)
  if special_number == 1:
    return True
  else:
    return False

def change_power(player, status):
  if status == 'special':
    playing_teams['myself'].attack *= 2
    playing_teams['myself'].defense *= 2
  elif status == 'normal':
    playing_teams['myself'].attack /= 2
    playing_teams['myself'].defense /= 2
 
def play():
  create_teams()
  show_teams()
  choice_team('myself')
  choice_team('enemy')
  score_boards = ['＿＿｜', '自分｜', '相手｜']
  is_special_inning = {}
  for i in range(9):
    score_boards[0] += str(i + 1) + '｜'
    is_special_inning[0] = get_special_inning()
    is_special_inning[1] = get_special_inning()
    if is_special_inning[0]:
      change_power('myself', 'special')
    if is_special_inning[1]:
      change_power('enemy', 'special')   
    # 表の攻撃
    inning_score = get_play_inning('front')
    score_boards[1] += str(inning_score) + '｜'
    playing_teams['myself'].total_score += inning_score
    # 裏の攻撃
    if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
      score_boards[2] += 'X｜'
    else:
      inning_score = get_play_inning('back')
      score_boards[2] += str(inning_score) + '｜'
      playing_teams['enemy'].total_score += inning_score
    if is_special_inning[0]:
      change_power('myself', 'normal')
    if is_special_inning[1]:
      change_power('enemy', 'normal')   
  score_boards[0] += 'R｜'
  score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
  score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'
  print(score_boards[0])
  print(score_boards[1])
  print(score_boards[2])

play()
