from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# Listbox : 여러가지 값을 관리하는 목록 위젯

listbox = Listbox(root, selectmode='extended', height=0)
# selectmode : single = 하나만 선택, extended = 여러 개 선택 가능
# height : listbox에 들어가있는 값을 한 번에 몇 개 보여줄 것인가 // 0 : 전체
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(END)  # 맨 뒤에 있는 항목을 삭제
    # listbox.delete(0)  # 맨 앞에 있는 항목을 삭제

    # 개수 확인
    # print('리스트에는', listbox.size(), '개가 있습니다.')

    # 항목 확인
    # print('1번째부터 3번째까지의 항목 : ', listbox.get(0, 2))  # .get(시작 idx, 끝 idx) // (사과, 딸기, 바나나)

    # 선택된 항목 확인
    print('현재 선택된 항목 : ', listbox.curselection())  # 인덱스 값을 반환 // (1, 2, 3)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
