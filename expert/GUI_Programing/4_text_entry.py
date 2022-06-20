from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

txt = Text(root, width=30, height=5)  # width 30, height 5 크기의 텍스트 입력창 생성
txt.pack()

txt.insert(END, '글자를 입력하세요')  # placeholder와 비슷한 기능

e = Entry(root, width=30)  # Entry의 경우, 줄바꿈(엔터키)이 안 됨. 한 줄에 값을 입력받을 때 사용하면 좋다.
e.pack()
e.insert(0, '한 줄만 입력하세요')

# 버튼을 클릭했을 때 text, entry의 값 조작하기


def btncmd():
    # 내용 출력
    print(txt.get('1.0', END))  # 1번째 라인, 0번째 컬럼 위치부터 END(마지막)까지 가져오기
    print(e.get())  # entry의 경우 한 줄 값이기 때문에 get만 사용하면 됨

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
