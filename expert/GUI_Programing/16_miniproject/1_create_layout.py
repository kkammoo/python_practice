from tkinter import *
import tkinter.ttk as ttk

from click import progressbar

root = Tk()
root.title('이미지 합치기')

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add = Button(file_frame, padx=5, pady=5, width=12, text='파일 추가')
btn_add.pack(side='left')
btn_del = Button(file_frame, padx=5, pady=5, width=12, text='선택 삭제')
btn_del.pack(side='right')

# 리스트 프레임 (파일 목록)
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended',  height=15,
                    yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text='저장 경로')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

path_txt = Entry(path_frame)
path_txt.pack(side='left', fill='x', expand=True, padx=5, pady=5,
              ipady=4)  # ipady : innerPadding Y

path_btn = Button(path_frame, text='찾아 보기', width=10)
path_btn.pack(side='right', padx=5, pady=5)

# 옵션 프레임 (가로 넓이, 간격, 포맷)
frame_option = LabelFrame(root, text='옵션')
frame_option.pack(fill='both', padx=5, pady=5, ipady=5)

# 옵션1) 가로 넓이
width_label = Label(frame_option, text='가로 넓이', width=8)
width_label.pack(side='left', padx=5, pady=5)

width_values = ['원본 크기', '1024', '800', '640']
width_combo = ttk.Combobox(frame_option, height=4,
                           state='readonly', width=10, values=width_values)
width_combo.current(0)
width_combo.pack(side='left', padx=5, pady=5)

# 옵션2) 간격
space_label = Label(frame_option, text='간격', width=8)
space_label.pack(side='left', padx=5, pady=5)

space_values = ['없음', '좁게', '보통', '넓게']
space_combo = ttk.Combobox(
    frame_option, height=4, state='readonly', width=10, values=space_values)
space_combo.current(0)
space_combo.pack(side='left', padx=5, pady=5)

# 옵션3) 저장 포맷
format_label = Label(frame_option, text='저장 포맷', width=8)
format_label.pack(side='left', padx=5, pady=5)

format_values = ['PNG', 'JPG', 'BMP']
format_combo = ttk.Combobox(frame_option, height=3,
                            state='readonly', width=10, values=format_values)
format_combo.current(0)
format_combo.pack(side='left', padx=5, pady=5)

# 진행상황 : 프로그레스 바
frame_progress = LabelFrame(root, text='진행 상황')
frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill='x', padx=5, pady=5)

# 실행 프레임
frame_action = Frame(root)
frame_action.pack(fill='x', padx=5, pady=5)

btn_exit = Button(frame_action, padx=5, pady=5,
                  width=12, text='닫기', command=root.quit)
btn_exit.pack(side='right')

btn_run = Button(frame_action, padx=5, pady=5, width=12, text='시작')
btn_run.pack(side='right')


root.resizable(False, False)
root.mainloop()
