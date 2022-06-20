import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# 콤보박스 : tkinter.ttk에 메소드가 들어있음 // select창 처럼 나옴
values = [str(i) + '일' for i in range(1, 32)]  # 1~31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일')  # 최초 목록의 제목 설정. // 버튼 클릭을 통한 값 설정도 가능

readonly_combobox = ttk.Combobox(
    root, height=10, values=values, state='readonly')  # state='readonly' 설정을 통해 콤보 박스의 value값의 임의 변경을 막을 수 있다.
readonly_combobox.current(0)  # 0 번째 인덱스 값을 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())  # 선택된 값 출력


btn = Button(root, text="확인", command=btncmd)
btn.pack()

root.mainloop()
