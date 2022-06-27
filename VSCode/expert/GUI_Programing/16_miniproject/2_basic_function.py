from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox

root = Tk()
root.title('이미지 합치기')


# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(
        title='이미지 파일을 선택하세요.', filetypes=(('PNG 파일', '*.png'), ('모든 파일', '*.*')), initialdir='C:/Users/rlaan/downloads')

    # 파일 목록 출력
    for file in files:
        list_file.insert(END, file)


# 선택 삭제
def del_file():
    # reversed : 배열의 뒤집한 값을 반환. 본래 배열엔 영향 없음
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장 경로
def save_path():
    save_path_dir = filedialog.askdirectory()
    if save_path_dir is None:
        return
    else:
        path_txt.delete(0, END)
        path_txt.insert(0, save_path_dir)


# 시작 버튼
def program_run():
    # 각 옵션의 값을 확인

    # 파일 목록 유무 확인
    if list_file.size() == 0:
        msgbox.showwarning('경고', '이미지 파일을 추가하세요.')
        return
    # 저장 경로 유무 확인
    elif len(path_txt.get()) == 0:
        msgbox.showwarning('경고', '저장 경로를 지정해주세요.')
        return


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add = Button(file_frame, padx=5, pady=5, width=12,
                 text='파일 추가', command=add_file)
btn_add.pack(side='left')
btn_del = Button(file_frame, padx=5, pady=5, width=12,
                 text='선택 삭제', command=del_file)
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

path_btn = Button(path_frame, text='찾아 보기', width=10, command=save_path)
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

btn_run = Button(frame_action, padx=5, pady=5, width=12,
                 text='시작', command=program_run)
btn_run.pack(side='right')


root.resizable(False, False)
root.mainloop()
