import time
from PIL import ImageGrab  # 파이썬 이미지 라이브러리

time.sleep(5)  # 실행 후 5초 대기

for i in range(1, 11):
    img = ImageGrab.grab()  # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i))  # 파일로 저장 (image1.png ~ image10.png)
    time.sleep(2)  # 2초 단위로
