# 자료 구조의 변경

# 커피숍
menu = {'커피', '우유', '주스'}
print(menu, type(menu)) # {} 타입은 set

menu = list(menu) # menu를 리스트 구조로 변경
print(menu, type(menu)) # 중괄호가 []로 바뀌고, 타입 또한 list로 변경된 것을 확인할 수 있다.

menu = tuple(menu)
print(menu, type(menu)) # 대괄호가 ()로 바뀌고, 타입 또한 tuple로 변경된 것을 확인할 수 있다.

menu = set(menu)
print(menu, type(menu)) # 소괄호가 {}로 바뀌고, 타입 또한 set으로 변경된 것을 확인할 수 있다.
