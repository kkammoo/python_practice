# 다중 상속 : 부모 class가 둘 이상. // 자바와는 달리, 파이썬에선 다중 상속을 지원한다.

# 일반 유닛
class Unit :
  def __init__(self, name, hp) :
    self.name = name
    self.hp = hp


# 공격 유닛
class AttackUnit(Unit):
  def __init__(self, name, hp, damage) :
    Unit.__init__(self, name, hp)
    self.damage = damage

  def attack(self, location) :
    print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

  def damaged(self, damage) :
    print('{0} : {1} 대미지를 입었습니다.'.format(self.name, damage))
    self.hp -= damage
    print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
    if self.hp <= 0 :
      print('{0} : 파괴되었습니다.'.format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격 기능은 없는 일반 유닛

# 공중 유닛
class Flyable : 
  def __init__(self, flying_speed) :
    self.flying_speed = flying_speed

  def fly(self, name, location) :
    print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable) : # AttackUnit class와 Flyable class를 다중 상속 받음
  def __init__(self, name, hp, damage, flying_speed) :
    AttackUnit.__init__(self, name, hp, damage) # AttackUnit class에서 name, hp, damage를,
    Flyable.__init__(self, flying_speed) # Flyable class에서 flying_speed를 가져와 사용

# 발키리 : 공중 공격 유닛, 한 번에 14발의 미사일을 발사.
valkyrie = FlyableAttackUnit('발키리', 200, 6 ,5)
valkyrie.fly(valkyrie.name, '3시')
