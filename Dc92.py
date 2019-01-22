import random

teams = []

class Team:
  def __init__(self, name, attack, defense):
    self.name = name
    self.attack = attack
    self.defense = defense

  def info(self):
    print(self.name + ': 攻撃力:' + str(self.attack) + ' / 守備力:' + str(self.defense))

def create_teams():
  global teams
  team1 = Team('アタッカーズ', 80, 20)
  team2 = Team('ディフェンダーズ', 30, 70)
  team3 = Team('アベレージーズ', 50, 50)
  teams = [team1, team2, team3]

def show_teams():
  index = 1
  print('全チームの情報')
  for team in teams:
    print(str(index))
    team.info()
    index += 1

def play():
  create_teams()
  show_teams()

play()
