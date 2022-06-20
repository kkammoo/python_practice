# for문
# 파이썬에서의 for문은 Java의 향상된 for문이랑 비슷하게 생겼다


# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
# print('대기번호 : 4')

for waiting_no in [1, 2, 3, 4] :
  print('대기번호 : {0}'.format(waiting_no))

print('==========')

# range()함수를 사용할 수도 있다.
for waiting_no in range(1, 6) :
  print('대기번호 : {0}'.format(waiting_no))

print('==========')

# 스타벅스에 손님이 왔다
starbucks = ['아이언맨', '토르', '그루트']

for customer in starbucks :
  print("{0}님, 주문하신 음료가 나왔습니다.".format(customer))
