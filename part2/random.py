# 랜덤 함수

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print('=================')

print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수 값 생성
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))

print('=================')

print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 정수 값 생성
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)

print('=================')

# randrange(a, b) 함수 : a ~ b 미만의 임의의 값 생성
print(randrange(1, 46)) 
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print('=================')

# randint(a, b) 함수 : a ~ b 이하의 임의의 값 생성
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
