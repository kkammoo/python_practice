from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')

btn1 = Button(root, text='버튼1')
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text='버튼2')
# padx/y 패딩 값 지정 (버튼 크기 유동적변화)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4')  # 버튼의 크기를 지정(고정)
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow',
              text='버튼5')  # fg : 폰트 색상, bg : 배경 색상
btn5.pack()

# 이미지로 버튼 만들기
photo = PhotoImage(file='GUI_Programing/img.png')
btn6 = Button(root, image=photo)
btn6.pack()


# 버튼을 눌렀을 때 이벤트 처리
def btncmd():
    print('버튼이 클릭되었습니다.')


btn7 = Button(root, text='동작하는 버튼', command=btncmd)
btn7.pack()

root.mainloop()
