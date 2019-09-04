import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

card_images = []
cards = []

def load_image():
  image_name = 'cards.jpg'
  vsplit_number = 4
  hsplit_number = 13
  
  if not os.path.isfile(image_name):
    response = requests.get('http://3156.bz/techgym/cards.jpg', allow_redirects=False)
    with open(image_name, 'wb') as image:
      image.write(response.content)
   
  img = cv.imread('./'+image_name)
  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
  h, w = img.shape[:2]
  crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
  
  card_images.clear()
  for h_image in np.vsplit(crop_img, vsplit_number):
    for v_image in np.hsplit(h_image, hsplit_number):
      card_images.append(v_image)

class Card:
  def __init__(self, mark, display_name, number, image):
    self.mark = mark
    self.display_name = display_name
    self.number = number
    self.image = image

def create_cards():
  cards.clear()
  marks = ['ハート', 'スペード', 'ダイヤ', 'クローバー']
  display_names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  for i, mark in enumerate(marks):
    for j, number in enumerate(numbers):
      cards.append( Card(mark, display_names[j], number, card_images[i*len(numbers)+j]) )

def show_card(card):
  print(f"{card.mark}{card.display_name}")
  plt.subplot(1,6,1)
  plt.axis("off")
  plt.imshow(card.image)
  plt.show()

def play():
  print('デバッグログ：play()')
  load_image()
  create_cards()
  show_card(cards[10])

play()
