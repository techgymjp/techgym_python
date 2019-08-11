import random

players = []
table = []
cells = []

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin
    self.is_hit = False
    self.is_double = False
    self.bets = {}
    self.reset_table()

  def set_bet_coin(self, bet_coin, bet_cell):
    self.coin -= bet_coin
    self.bets[bet_cell] = bet_coin
    print(self.name + 'は ' + str(bet_coin) + 'コイン を ' + bet_cell + ' にBETしました。')

  def reset_table(self):
    if not self.is_double:
      for cell in table:
        self.bets.update({cell.name: 0})

  def double(self):
    for key, bet in self.bets.items():
      self.bets[key] *= 2
      self.coin -= int(bet)

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    if self.coin >= 99:
      max_bet_coin = 99
    else:
      max_bet_coin = self.coin
    bet_message = '何枚BETしますか？：(1-' + str(max_bet_coin) + ')'
    bet_coin = input(bet_message)
    while not self.enable_bet_coin(bet_coin, max_bet_coin):
      bet_coin = input(bet_message)

    bet_message = 'どこにBETしますか？：(R,B,1-8)'
    bet_cell = input(bet_message)
    while not self.enable_bet_cell(bet_cell):
      bet_cell = input(bet_message)
 
    super().set_bet_coin(int(bet_coin), bet_cell)

  def enable_bet_coin(self, string, max_bet_coin):
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= max_bet_coin:
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

  def get_double_up(self):
    double_message = 'ダブルアップしますか？：(Y or N)'
    input_double = input(double_message)
    print(input_double)
    print(self.enable_double(input_double))
    while not self.enable_double(input_double):
      input_double = input(double_message)
    if input_double == 'Y':
      return True
    else:
      return False

  def enable_double(self, string):
    if string == 'Y' or string == 'N':
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

    bet_cell_number = random.randint(0, len(cells) - 1)
    bet_cell = cells[bet_cell_number]
    super().set_bet_coin(bet_coin, bet_cell)

  def get_double_up(self):
    double_number = random.randint(1, 2)
    if double_number == 1:
      return True
    else:
      return False

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

def set_cells():
  global cells
  cells = []
  for cell in table:
    cells.append(cell.__dict__['name'])

def create_players():
  global players
  human = Human('MY', 500)
  computer1 = Computer('C1', 500)
  computer2 = Computer('C2', 500)
  computer3 = Computer('C3', 500)
  players = [human, computer1, computer2, computer3]

def bet_players():
  for player in players:
    if not player.is_double:
      player.bet()

def check_double_player():
  global players
  for player in players:
    player.is_double = False
    if player.is_hit:
      player.is_double = player.get_double_up()

def bet_double():
  for player in players:
    if player.is_double:
      player.double()

def check_hit():
  global players
  hit_cell_number = random.randint(2, len(cells) - 1)
  hit_cell = cells[hit_cell_number]
  print('選ばれたのは「' + hit_cell + '」')
  for player in players:
    player.is_hit = False
    if player.bets[hit_cell] >= 1:
      player.is_hit = True
      win_player(player, hit_cell_number)
    if table[hit_cell_number].color == 'red':
      hit_cell_color = 'R'
      hit_cell_color_number = 0
    else:
      hit_cell_color = 'B'
      hit_cell_color_number = 1
    if player.bets[hit_cell_color] >= 1:
      player.is_hit = True
      win_player(player, hit_cell_color_number)

def win_player(player, hit_cell_number):
  hit_cell = cells[hit_cell_number]
  win_coin = player.bets[hit_cell] * table[hit_cell_number].rate
  player.coin += win_coin
  print(player.name + 'は当たり ' + str(win_coin) + 'コインを獲得しました。')

def show_coin():
  message = '[持ちコイン] '
  for player in players:
    message += player.name + ':' + str(player.coin) + ' / '
  print(message)

def create_table():
  global table
  table.append(Cell('R', 2, 'red'))
  table.append(Cell('B', 2, 'black'))
  table.append(Cell('1', 8, 'red'))
  table.append(Cell('2', 8, 'black'))
  table.append(Cell('3', 8, 'red'))
  table.append(Cell('4', 8, 'black'))
  table.append(Cell('5', 8, 'red'))
  table.append(Cell('6', 8, 'black'))
  table.append(Cell('7', 8, 'red'))
  table.append(Cell('8', 8, 'black'))

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

def reset_table():
  for player in players:
    player.reset_table()

def color(color_name, string):
  if color_name == 'red':
    return ColorBase.RED + string + ColorBase.END
  elif color_name == 'green':
    return ColorBase.GREEN + string + ColorBase.END
  else:
    return string

def green_bar():
  return color('green', '｜')

def initialize():
  create_table()
  create_players()
  set_cells()

def play_once():
  reset_table()
  bet_players()
  show_table()
  check_hit()
  check_double_player()
  bet_double()
  show_coin()

def is_game_end():
  for player in players:
    if player.coin <= 0:
      return True
  return False

def game_end():
  for player in players:
    if player.coin <= 0:
      print(player.name + 'のコインがなくなったためゲームを終了します。')

def play():
  initialize()
  show_coin()
  while not is_game_end():
    play_once()
  else:
    game_end()

play()
