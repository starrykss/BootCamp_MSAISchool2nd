# Lab 06. 동영상 데이터에서 원하는 프레임 만큼 이미지 추출 실습

import cv2
import os

cap = cv2.VideoCapture('홈페이지 배경 샘플 영상 - 바다.mp4')

img_count = 0

os.makedirs("./video_frame_dataset/", exist_ok=True)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if img_count % 30 == 0:
        img_filename = f"./video_frame_dataset/frame_{img_count:04}.png"
        cv2.imwrite(img_filename, frame)

    img_count += 1

cap.release()