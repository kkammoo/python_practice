from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# radio 버튼 : 여러 개의 버튼 중 택1
# 라디오 버튼 그루핑
Label(root, text='메뉴를 선택하세요.').pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)
btn_burger1.select()  # 햄버거 항목이 초기값으로 선택되어 있음
btn_burger2 = Radiobutton(root, text='치즈버거', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='치킨버거', value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text='음료를 선택하세요.').pack()
drink_var = StringVar()  # value가 문자열일 땐 variable 값을 String으로
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항목의 value값을 출력
    print(drink_var.get())  # 음료 중 선택된 라디오 항목의 value값을 출력


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
