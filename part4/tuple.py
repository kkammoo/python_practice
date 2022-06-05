# 튜플 : 리스트보다 처리속도가 빠르지만 값의 변경이 불가능하다

menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])

# menu.add('생선까스') 값 추가 안 됨.

name = '김종국'
age = 20
hobby = '코딩'
print(name, age, hobby)

(name, age, hobby) = ('김종국', 20, '코딩')
print(name, age, hobby)
