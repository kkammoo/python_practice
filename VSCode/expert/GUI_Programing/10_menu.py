from tkinter import *

from click import progressbar

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표


def create_new_file():
    print('새 파일을 만듭니다')


# 메뉴바 생성
menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='New File', command=create_new_file)
menu_file.add_command(label='New Window')
menu_file.add_separator()  # 구분선
menu_file.add_command(label='Open File...')
menu_file.add_separator()
menu_file.add_command(label='Save All', state='disable')
# state='disable' : 선택 비활성화
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.quit)

menu.add_cascade(label='File', menu=menu_file)

# Edit 메뉴
menu.add_cascade(label='Edit')

# Language 메뉴 (라디오 버튼)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='Java')
menu_lang.add_radiobutton(label='C++')

menu.add_cascade(label='Language', menu=menu_lang)

# View 메뉴 추가 (체크 박스)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu_view.add_checkbutton(label='Show Breadcrumbs')

menu.add_cascade(label='View', menu=menu_view)


root.config(menu=menu)
root.mainloop()
