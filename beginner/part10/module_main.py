# 모듈 불러오기 : import 모듈


# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때 가격


# 모듈을 불러올 때 별칭을 지정 : import 모듈 as 별칭
# import theater_module as mv
# 모듈 명이 길 때, 별칭을 사용하면 모듈 내 클래스, 함수를 불러올 때 보다 간결한 단어로 모듈을 이용할 수 있다.
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# from문을 이용 : from 모듈 import 클래스/함수/*(전체)
# from theater_module import *
# from문을 이용하면 .방식으로 클래스/함수를 불러오는 것이 아닌, 있는 그대로 사용할 수 있음.
# price(3)
# price_morning(4)
# price_soldier(5)


# from문을 이용하여 특정 함수만 가져오기
# from theater_module import price, price_morning
# price(3)
# price_morning(4)


# 불러오는 함수에 별칭 지정하기
from theater_module import price_soldier as ps
ps(5)
