import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('이미지 합치기')
root.geometry('640x480+300+300')  # 가로X세로 x좌표, y좌표

# 메시지 박스 : 예를 들어, 에러가 떴을 때 나오는 팝업 같은 것. 보면 앎


# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.')  # 파란색 동그라미 모양의 info의 i 아이콘


def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다.')  # 노란색 삼각형 모양의 ! 아이콘


def err():
    msgbox.showerror('에러', '잘못된 입력입니다.')  # 빨간색 동그라미 모양의 X 아이콘 (소리도 다름)


def okcancel():
    msgbox.askokcancel('확인/취소', '해당 좌석은 유아동반석 입니다. 예매하시겠습니까?')
    # 파란색 동그라미 모양의 ? 아이콘, 확인 / 취소 버튼의 메시지창


def retrycancel():
    msgbox.askretrycancel('재시도/취소', '일시적인 오류입니다. 다시 시도하시겠습니까?')
    # 노란색 삼각형 모양의 ! 아이콘, 다시 시도 / 취소 버튼의 메시지창


def yesno():
    msgbox.askyesno('예/아니오', '해당 좌석은 역방향입니다. 예매하시겠습니까?')
    # 파란색 동그라미 모양의 ? 아이콘, 예 / 아니오 버튼의 메시지창


def yesnocancel():
    response = msgbox.askyesnocancel(
        title=None, message='예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?')
    # 파란색 동그라미 모양의 ? 아이콘, 예 / 아니오 / 취소 버 튼의 메시지창
    # 네 : 저장 후 종료, 아니오 : 저장 안 하고 종료, 취소 : 프로그램 종료 취소 (현재 화면)
    # response 응답 : True, False, None = 예 : 1, 아니오 : 0, 취소 : 그 외
    if response == 1:
        print('예')
    elif response == 0:
        print('아니오')
    else:
        print('취소')


Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=err, text='에러').pack()

Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesnocancel, text='예 아니오 취소').pack()


root.mainloop()
