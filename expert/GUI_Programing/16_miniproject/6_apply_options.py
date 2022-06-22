from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os
import time

root = Tk()
root.title('이미지 합치기')


# 이미지 통합
def merge_image():
    try:
        # 옵션1) 가로 넓이
        img_width = width_combo.get()
        if img_width == '원본 크기':
            img_width = -1  # -1일 때엔 원본 기준으로.
        else:
            img_width = int(img_width)

        # 옵션2) 간격
        img_space = space_combo.get()
        if img_space == '좁게':
            img_space = 30
        elif img_space == '보통':
            img_space = 60
        elif img_space == '넓게':
            img_space = 90
        else:  # 간격 없음
            img_space = 0

        # 옵션3) 저장 포맷
        img_format = format_combo.get().lower()  # PNG, JPG, BMP 값을 소문자로 변경

        ##########################################################################

        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈를 리스트에 넣어서 하나씩 처리
        image_sizes = []  # [(width, height), (width2, height2), ...]
        if img_width > -1:
            # width 값 변경

            # 넓이에 따른 높이 계산 (비례식)
            # 변경 height = (원본 height * 변경 width) / 원본 width
            image_sizes = [int(img_width), int(
                img_width * x.size[1] / x.size[0] for x in images)]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(
            heights)  # 합치는 사진의 최대 넓이, 전체 높이 구하기

        # 최종 결과물 생성
        if img_space > 0:
            # 간격 값이 있으면 전체 길이에 이미지 개수 -1 만큼 간격을 넣어줘야 함
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new(
            'RGB', (max_width, total_height), (255, 255, 255))  # 배경 흰색

        y_offset = 0  # y 위치

        for idx, img in enumerate(images):
            # width가 원본 유지가 아닐 때에는 이미지 크기를 조정해줘야 한다.
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            # height 값 만큼 더해줌 + 간격이 있으면 간격까지
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100  # 실제 % 정보 계산
            p_var.set(progress)
            progress_bar.update()

        # 저장 포맷 옵션
        curr_time = time.strftime('_%Y%m%d_%H%M%S')
        file_name = 'merge_photo{}.'.format(curr_time) + img_format
        save_path_dir = os.path.join(path_txt.get(), file_name)
        result_img.save(save_path_dir)
        msgbox.showinfo('알림', '작업이 완료되었습니다.')
    except Exception as err:
        msgbox.showerror('에러', err)


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
    if save_path_dir == '':
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
    # 이미지 통합 작업
    merge_image()


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
