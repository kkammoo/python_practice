def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='게스트'):
    hands = ['바위', '가위', '보']
    print(name + '(은)는' + hands[hand] + '를 냈습니다.')

def judge(player, computer):
    if player == computer:
        return '무승부'
    elif player == 0 and computer == 1:
        return '승리'
    elif player == 1 and computer == 2:
        return '승리'
    elif player == 2 and computer == 0:
        return '승리'
    else:
        return '패배'
