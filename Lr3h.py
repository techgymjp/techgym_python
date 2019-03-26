import random

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

  def info(self):
    print(self.name + '：' + str(self.coin))

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    bet_coin = input('何枚BETしますか？：(1-99)')
    print(bet_coin)

def play():
  print('デバッグログ：play()')
  
  human = Human('MY', 500)
  human.info()

  human.bet()

play()
