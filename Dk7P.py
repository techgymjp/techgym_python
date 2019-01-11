import random

level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def play():
  section_message()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)

start_message()
play()
