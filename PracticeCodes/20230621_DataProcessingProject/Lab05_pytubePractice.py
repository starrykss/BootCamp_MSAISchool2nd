# Lab 05. 동영상 데이터(유튜브 영상) 추출 실습

from pytube import YouTube
from IPython.display import HTML

url = "https://www.youtube.com/watch?v=ILqJOHYYlkc"

yt = YouTube(url)

stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()    # 최고 해상도로 가져온다.

stream.download()

# HTML("""
# <video width="640" height="480" controls>
#     <source src="./홈페이지 배경 샘플 영상 - 바다.mp4" type="video/mp4">
# </video>
# """
# )