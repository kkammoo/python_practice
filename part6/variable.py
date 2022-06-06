# 지역변수, 전역변수
# 자바, 자바스크립트와 달리 파이썬에서 전역 변수를 함수 내에서 사용하기 위해선 global 명령어를 통해 전역변수를 불러와야 함

gun = 10

# 전역 변수 활용 case 1) global
def check_point(soldiers) : # 경계근무
  global gun # 전역 변수 gun을 함수 내에서 사용
  gun = gun - soldiers
  print('[함수 내] 남은 총 : {0}'.format(gun))

print('전체 총 : {0}'.format(gun))
check_point(2) # 2명이 경계 근무 나감
print('남은 총 : {0}'.format(gun))

# 전역 변수 활용 case 2) return문
def check_point_return(gun, soldiers) :
  gun = gun - soldiers
  print('[함수 내] 남은 총 : {0}'.format(gun))
  return gun

print('전체 총 : {0}'.format(gun))
gun = check_point_return(gun, 2) # 2명이 경계 근무 나감
print('남은 총 : {0}'.format(gun))
