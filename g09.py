from google.colab import files

uploaded_file = files.upload()
uploaded_file_name = next(iter(uploaded_file))

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(uploaded_file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#オブジェクトimgのshapeメソッドの1つ目の戻り値(画像の高さ)をimg_heightに、2つ目の戻り値(画像の幅)をimg_widthに代入
img_height,img_width=img.shape[:2]  
print(img.shape)
height = img.shape[0]
width = img.shape[1]

scale_factor = 0.05 #縮小処理時の縮小率(小さいほどモザイクが大きくなる)
img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor) #縮小率の倍率で画像を縮小
#画像を元の画像サイズに拡大。ここで補完方法に'cv2.INTER_NEAREST'を指定することでモザイク状になる
img = cv2.resize(img, (img_width, img_height),interpolation=cv2.INTER_NEAREST)


plt.imshow(img) #表示