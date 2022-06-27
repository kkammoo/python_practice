from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# checkbox (Checkbutton)
chkvar = IntVar()  # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar)
# chkbox.select() # 체크박스 자동 선택
# chkbox.deselect() # 체크박스 선택 해제 (default값)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일 동안 보지 않기', variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0 : 체크해제, 1 : 체크
    print(chkvar2.get())  # 0 : 체크해제, 1 : 체크


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
