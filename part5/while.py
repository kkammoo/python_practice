# while문

# while 조건식 :
#     실행 명령문
#     증감식

customer = '토르'
index = 5
while index >= 1 :
  print('{0}님, 주문하신 음료 나왔습니다. {1}잔 남았습니다.'.format(customer, index))
  index -= 1
  if index == 0 :
    print('{0}님, 주문하신 음료 나왔습니다.'.format(customer))
    print('마지막 음료까지 다 나왔습니다.')


# 무한 루프
customer = '아이언맨'
index = 1
while True :
  print('{0}님, 주문하신 음료 나왔습니다. {1}번 호출'.format(customer, index))
  index += 1
