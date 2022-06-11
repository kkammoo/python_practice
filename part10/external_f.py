# 외장 함수 : import를 해야지 사용할 수 있는 함수
# docs.python.org -> list of python modules -> Python Module Index

# glob : 경로 내의 폴더/파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob('*.py')) # 확장자가 .py인 모든 파일의 list를 출력


# os : 운영체제에서 제공하는 기본 기능
import datetime
import time
import os
print(os.getcwd())  # 현재 디렉토리 표시

folder = 'sample_dir'

if os.path.exists(folder):
    print('이미 존재하는 폴더입니다.')
else:
    print('폴더가 존재하지 않습니다.')


# time, datetime : 시간 관련 함수
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

print('오늘 날짜는', datetime.date.today())

today = datetime.date.today()  # 오늘 날짜 저장

# timedelta : 두 날짜 사이의 간격 // 오늘 날짜로부터 100일 뒤 저장
td = datetime.timedelta(days=100)

print('우리가 만난지 100일 되는 날은', today + td)
