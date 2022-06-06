# 함수 

# def 함수 이름() :
#   실행 명령문

def open_account() :
  print('새로운 계좌가 생성되었습니다')

# 함수 실행 : 함수이름()
open_account()

def deposit(balance, money) : # 입금
  print('입금이 완료되었습니다. 잔액은 {0} 원 입니다.'.format(balance + money))
  return balance + money


def withdraw(balance, money) : # 출금
  if balance >= money : 
    print('출금이 완료되었습니다. 잔액은 {0} 원 입니다.'.format(balance - money))
    return balance - money
  else : 
    print('잔액이 부족합니다. 잔액은 {0} 원 입니다.'.format(balance))
    return balance

def withdraw_night(balance, money) : # 야간 수수료
  commission = 100 # 야간 수수료 100원
  return commission, balance - money - commission


balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)

# balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
print(balance)

commission, balance = withdraw_night(balance, 300)
print('출금이 완료되었습니다. 수수료는 {0} 원이며, 잔액은 {1} 원 입니다.'.format(commission, balance))
print(balance)

