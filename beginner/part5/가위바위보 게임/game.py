import utils
import random

print('가위바위보 게임을 시작합니다')
player_name = input('플레이어 이름을 입력해주세요. : ')
print('무엇을 내겠습니까? 0: 바위, 1: 가위, 2: 보）')
player_hand = int(input('숫자를 입력해주세요. : '))

if utils.validate(player_hand):
  
  computer_hand = random.randint(0, 2)

  if player_name == '':
    utils.print_hand(player_hand)
  else:
    utils.print_hand(player_hand, player_name)

  utils.print_hand(computer_hand, '컴퓨터')
  
  result = utils.judge(player_hand, computer_hand)
  print('결과는 ' + result + ' 입니다.')
else:
  print('올바른 값을 입력해주세요.')
