'''
당신은 kakako 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1) 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
조건 2) 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

출력문 예제)
[o] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[o] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승객 : 2명
'''

from random import *

total_customer = 0 # 총 탑승객

for customer in range(1,51) : 
  time = randrange(5, 50)
  if 5 <= time <= 15 :
    print('[o] {0}번 손님 (소요시간 : {1}분)'.format(customer, time))
    total_customer += 1
  else :
    print('[ ] {0}번 손님 (소요시간 : {1}분)'.format(customer, time))
  
print('총 탑승객 : {0}명'.format(total_customer))


