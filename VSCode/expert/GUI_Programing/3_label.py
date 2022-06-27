from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')

# 레이블의 경우, 글자 혹은 이미지를 보여준다고만 생각하면 된다.

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file='GUI_Programing/img.png')
label2 = Label(root, image=photo)
label2.pack()

# 버튼을 눌렀을 때 label 값을 변경


def change():
    label1.config(text='또 만나요')

    global photo2  # photo2를 전역변수로 설정해야지만 버튼을 눌렀을 때 이미지가 바뀐다. Garbage Collection을 피함
    photo2 = PhotoImage(file='GUI_Programing/img2.png')
    label2.config(image=photo2)


btn = Button(root, text='클릭', command=change)
btn.pack()
root.mainloop()
