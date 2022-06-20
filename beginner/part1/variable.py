# 파이썬의 변수 : 직관적인 단어로. 두 단어 이상의 변수는 _(언더바)로 구분

print('우리집 강아지의 이름은 연탄이에요')
print('연탄이는 4살이며, 산책을 아주 좋아해요')
print('연탄이는 어른일까요? True')

print('============')

animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요')
print(name + '는 ' + str(age) + '살이며, '+ hobby + '을 아주 좋아해요') # 문자열 사이에 정수형 값은 문자열로 변환해줘야 한다. str(정수형 변수)
print(name +'는 어른일까요? '+str(is_adult)) # boolean 타입도 문자열로 출력할 때엔 값을 문자열로 변환해줘야 한다.

print('============')

animal = '고양이'
name = '해피'
age = 2
hobby = '낮잠'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요')
hobby = '공놀이'  # 변수 hobby 값 변경
print(name + '는 ' + str(age) + '살이며, '+ hobby + '을 아주 좋아해요')
print(name +'는 어른일까요? '+str(is_adult))

print('============')

print('우리집 ' + animal + '의 이름은 ' + name + '에요')
print(name, '는 ', age, '살이며, ', hobby, '을 아주 좋아해요') # + 연산자가 아닌 , 를 이용하면 형변환을 안 해줘도 된다. (띄어쓰기가 되는 게 함정)
print(name +'는 어른일까요? '+str(is_adult))
