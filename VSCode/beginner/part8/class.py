# 클래스 (자바의 class 그거임)

# 스타크래프트로 예를 들어

# 마린 : 공격 유닛, 군인(명사), 총을 쏠 수 있음(동사)
name = '마린' # 유닛 이름
hp = 40 # 유닛 체력
damage = 5 # 유닛 공격력

print('{0} 생성되었습니다'.format(name))
print('체력 : {0}, 공격력 : {1}\n'.format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데 일반/시즈 모드가 있음.
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{0} 생성되었습니다'.format(tank_name))
print('체력 : {0}, 공격력 : {1}\n'.format(tank_hp, tank_damage))

def attack(name, location, damage) :
  print('{0} : {1} 방향으로 적군을 공격합니다 [공격력 {2}]'.format(name, location, damage))

attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)

# 탱크를 하나 더 추가한다면?
tank2_name = '탱크'
tank2_hp = 150
tank2_damage = 35

attack(tank2_name, '1시', tank2_damage) # 이런식으로 계속 추가하게 되면 너무 비효율적인 코딩
