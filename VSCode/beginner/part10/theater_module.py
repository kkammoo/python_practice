# 모듈 : class 정의나 함수 정의를 담고 있는 파일 .py

# 극장에 있다고 가정. 이곳은 현금만 받음. 잔돈 안 바꿔줌

# 일반 가격
def price(people):
    print('{0}명 가격은 {1}원 입니다.'.format(people, people*10000))


# 조조할인 가격
def price_morning(people):
    print('{0}명 조조 할인 가격은 {1}원 입니다.'.format(people, people*6000))


# 군인할인 가격
def price_soldier(people):
    print('{0}명 군인 할인 가격은 {1}원 입니다.'.format(people, people*4000))
