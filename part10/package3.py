# 패키지, 모듈 위치 확인
# import inspect // inspect.getfile()


from travel import *
import inspect
import random

print(inspect.getfile(random))  # random.py의 파일 경로가 출력된다

print(inspect.getfile(thailand))
