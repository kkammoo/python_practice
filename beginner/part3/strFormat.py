# 문자열 포맷

print('a' + 'b')
print('a', 'b')

# case 1)
print('나는 %d살 입니다' %20) # %d는 정수값 (integer)

# case 2)
print('나는 %s을 좋아합니다' %'파이썬') # %s는 문자열 (string)

# case 3)
print('Apple은 %c로 시작합니다' %'A') # %c는 문자 (character)

# case 4)
print('나는 %s살 입니다' %20) # %s는 정수형, 문자도 올 수 있다

# case 5)
print('나는 %s색과 %s색을 좋아합니다' %('파란', '빨간')) # 복수의 값을 넣을 땐 소괄호로 묶기

print('==========')

# case 6) format()
print('나는 {}살 입니다'.format(20)) # 매개값이 중괄호에 들어간다.
print('나는 {}색과 {}색을 좋아합니다'.format('파란', '빨간')) # format에서 복수의 값을 넣을 땐 매개값으로 다 적어주면 됨

print('==========')

print('나는 {0}색과 {1}색을 좋아합니다'.format('파란', '빨간')) # {}에 숫자를 적으면 format의 매개값이 번호 순서대로 들어간다
print('나는 {1}색과 {0}색을 좋아합니다'.format('파란', '빨간')) 

print('==========')

print('나는 {age}살이며, {color}색을 좋아합니다'.format(age = 20, color = '빨간')) # 변수처럼 지정을 해주면 순서 상관 없이 해당 변수에 값이 들어감
print('나는 {age}살이며, {color}색을 좋아합니다'.format(color = '빨간', age = 20))

print('==========')
# 파이썬 버전 3.6이상부터 사용 가능
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아합니다')
