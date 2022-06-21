from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# 프레임 : 틀, 테두리

Label(root, text='메뉴를 선택해주세요').pack(side='top')

Button(root, text='주문하기').pack(side='bottom')

# 메뉴 프레임
frame_burger = Frame(root, relief='solid', bd=1)
# relief : 테두리 모양, bd : 테두리 굵기
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

# 음료 프레임
frame_drink = LabelFrame(root, text='음료')
frame_drink.pack(side='right', fill='both', expand=True)

Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop()
