import time
import tkinter.ttk as ttk
from tkinter import *

from click import progressbar

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# 프로그래스 바 : 진행 상황을 나타냄 // 프로그래스 바도 tkinter.ttk에 있음
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
# # mode = indeterminate : 로딩하는 느낌. determinate : 다운로드를 하는 느낌
# progressbar.start(10)  # 10 밀리세컨드마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()  # 실수 타입
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):  # 1~100
        time.sleep(0.01)  # 0.01초 대기
        p_var2.set(i)  # progressbar의 값 설정
        progressbar2.update()  # ui업데이트
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
