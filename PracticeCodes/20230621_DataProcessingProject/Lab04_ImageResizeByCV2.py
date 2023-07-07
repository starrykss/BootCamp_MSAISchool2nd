# Lab 04. 이미지 데이터 수집 방법 : 데이터 증강 기법 - 이미지 비율에 맞게 리사이즈 작업

import cv2
import numpy as np

img = cv2.imread("mango_img_dataset\\0000_mango.png")
print(img.shape)
# 250, 250 정사각 비율로 변환한다고 가정
cv2.imshow("", img)
cv2.waitKey()
cv2.destroyAllWindows()
h, w, c = img.shape  # h = 183, w = 275

black_bg = np.zeros((275, 275, 3))
start_h = (275 - h) // 2
black_bg[start_h:start_h + h, :] = img

# resized_img = cv2.resize(img, (275, 275))
cv2.imshow("", black_bg)
cv2.waitKey()
cv2.destroyAllWindows()