from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# 그리드 : 지정된 좌표에 요소 배치

# btn1 = Button(root, text='버튼1')
# btn2 = Button(root, text='버튼2')
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 그리드를 이용하여 키패드 만들기
# 1라인
btn_f16 = Button(root, text='F16', width=5, height=2)
btn_f17 = Button(root, text='F17', width=5, height=2)
btn_f18 = Button(root, text='F18', width=5, height=2)
btn_f19 = Button(root, text='F19', width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
# sticky : N, E, W, S 방향으로 붙이기
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 2라인
btn_clear = Button(root, text='clear', width=5, height=2)
btn_equal = Button(root, text='=', width=5, height=2)
btn_div = Button(root, text='/', width=5, height=2)
btn_mul = Button(root, text='*', width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 3라인
btn_7 = Button(root, text='7', width=5, height=2)
btn_8 = Button(root, text='8', width=5, height=2)
btn_9 = Button(root, text='9', width=5, height=2)
btn_sub = Button(root, text='-', width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4라인
btn_4 = Button(root, text='4', width=5, height=2)
btn_5 = Button(root, text='5', width=5, height=2)
btn_6 = Button(root, text='6', width=5, height=2)
btn_add = Button(root, text='+', width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 5라인
btn_1 = Button(root, text='1', width=5, height=2)
btn_2 = Button(root, text='2', width=5, height=2)
btn_3 = Button(root, text='3', width=5, height=2)
btn_enter = Button(root, text='enter', width=5, height=2)  # 세로로 2칸 사용

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)
# rowspan : 현재 위치로부터 아래쪽으로 몇 줄을 더함

# 6라인
btn_0 = Button(root, text='0', width=5, height=2)  # 가로로 2칸 사용
btn_point = Button(root, text='.', width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
# columnspan : 현재 위치로부터 오른쪽으로 몇 칸을 더함
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()
