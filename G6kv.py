import random

players = []
table = []

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin
    self.bets = {}
    for cell in table:
      self.bets.update({cell.name: 0})

  def info(self):
    print(self.name + '：' + str(self.coin))

  def set_bet_coin(self, bet_coin):
    self.coin -= bet_coin
    print(self.name + 'は ' + str(bet_coin) + 'コイン BETしました。')

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    bet_message = '何枚BETしますか？：(1-99)'
    bet_coin = input(bet_message)
    while not self.enable_bet_coin(bet_coin):
      bet_coin = input(bet_message)

    bet_message = 'どこにBETしますか？：(R,B,1-8)'
    bet_cell = input(bet_message)
    while not self.enable_bet_cell(bet_cell):
      bet_cell = input(bet_message)
 
    super().set_bet_coin(int(bet_coin))

  def enable_bet_coin(self, string):
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= 99:
        return True
      else:
        return False
    else:
      return False

  def enable_bet_cell(self, string):
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= 8:
        return True
      else:
        return False
    else:
      if string == 'R' or string == 'B':
        return True
      else:
        return False

class Computer(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    if self.coin >= 99:
      max_bet_coin = 99
    else:
      max_bet_coin = self.coin
    bet_coin = random.randint(1, max_bet_coin)
    cells = []
    for cell in table:
      cells.append(cell.__dict__['name'])
    bet_cell_number = random.randint(0, len(cells) - 1)
    bet_cell = cells[bet_cell_number]
    super().set_bet_coin(bet_coin)

class Cell:
  def __init__(self, name, rate, color):
    self.name = name
    self.rate = rate
    self.color = color

class ColorBase:
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  END = '\033[0m'

def create_players():
  global players
  human = Human('MY', 500)
  computer1 = Computer('C1', 500)
  computer2 = Computer('C2', 500)
  computer3 = Computer('C3', 500)
  players = [human, computer1, computer2, computer3]

def create_table():
  global table
  table.append(Cell('R', 8, 'red'))
  table.append(Cell('B', 8, 'black'))
  table.append(Cell('1', 2, 'red'))
  table.append(Cell('2', 2, 'black'))
  table.append(Cell('3', 2, 'red'))
  table.append(Cell('4', 2, 'black'))
  table.append(Cell('5', 2, 'red'))
  table.append(Cell('6', 2, 'black'))
  table.append(Cell('7', 2, 'red'))
  table.append(Cell('8', 2, 'black'))

def show_table():
  row = green_bar() + '____' + green_bar()
  for player in players:
    row += player.name + green_bar()
  print(row)
 
  for cell in table:
    row = green_bar() + color(cell.color, cell.name + '(x' + str(cell.rate) + ')') + green_bar()
    for player in players:
      row += str(player.bets[cell.name]).zfill(2) + green_bar()
    print(row)

def color(color_name, string):
  if color_name == 'red':
    return ColorBase.RED + string + ColorBase.END
  elif color_name == 'green':
    return ColorBase.GREEN + string + ColorBase.END
  else:
    return string

def green_bar():
  return color('green', '｜')

def play():
  print('デバッグログ：play()')
  create_table()
  create_players()
  show_table()
  players[1].bet()
  #show_players()

def show_players():
  for player in players:
    player.info()
  
  for player in players:
    player.bet()
 
  for player in players:
    player.info()

play()
