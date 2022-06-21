from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

listbox = Listbox(frame, selectmode='extend', height=10,
                  yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()
