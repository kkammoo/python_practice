import starcraft
from random import *

# 게임 진행
starcraft.game_start()

# 마린 3기 생성
m1 = starcraft.Marine()
m2 = starcraft.Marine()
m3 = starcraft.Marine()

# 탱크 2기 생성
t1 = starcraft.Tank()
t2 = starcraft.Tank()

# 레이스 1기 생성
w1 = starcraft.Wraith()

#  유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move('1시')

# 탱크 시즈모드 개발
starcraft.Tank.seize_developed = True
print('[알림] 탱크의 시즈 모드 개발이 완료되었습니다.')

# 공격 모드 준비 (탱크 : 시즈모드, 레이스 : 클로킹, 마린 : 스팀팩)
for unit in attack_units:
    if isinstance(unit, starcraft.Marine):
        unit.stimpack()
    elif isinstance(unit, starcraft.Tank):
        unit.set_seize_mode()
    elif isinstance(unit, starcraft.Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack('1시')

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))  # 공격은 랜덤으로 받음. (5~20)

# 게임 종료
starcraft.game_over()
