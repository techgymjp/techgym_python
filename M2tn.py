import random

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

def play():
  print('デバッグログ：play()')
  
  human = Human('MY', 500)

play()
