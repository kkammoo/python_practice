'''
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건 1) 표준 체중은 별도의 함수 내에서 계산한다.
* 함수명 : std_weight
* 전달값 : 키(height), 성별(gender)

조건 2) 표준 체중은 소수점 둘 째 자리까지 표시

출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

weight = 0

def std_weight(height, gender) :
  global weight

  if gender == '남자' :
    weight = round(((height / 100) * (height / 100) * 22), 2)
    print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))
  else :
    weight = round(((height / 100) * (height / 100) * 21), 2)
    print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))

# 남자 170cm
std_weight(170, '남자')

# 남자 185cm
std_weight(185, '남자')

# 여자 163cm
std_weight(163, '여자')

# 여자 158cm
std_weight(158, '여자')
