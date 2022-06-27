# 메소드 오버라이딩 : 부모 클래스의 메소드를 상속 받은 자식 클래스에서 해당 메소드를 재정의(같은 이름의 메소드를 부모 클래스와는 다른 기능으로)

# 일반 유닛
class Unit :
  def __init__(self, name, hp, speed) :
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location) :
    print('[지상 유닛 이동]')
    print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage) :
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

  def attack(self, location) :
    print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

  def damaged(self, damage) :
    print('{0} : {1} 대미지를 입었습니다.'.format(self.name, damage))
    self.hp -= damage
    print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
    if self.hp <= 0 :
        print('{0} : 파괴되었습니다.'.format(self.name))

# 공중 유닛
class Flyable :
  def __init__(self, flying_speed) :
    self.flying_speed = flying_speed

  def fly(self, name, location) :
    print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable) :
  def __init__(self, name, hp, damage, flying_speed) :
    AttackUnit.__init__(self, name, hp, 0, damage)
    Flyable.__init__(self, flying_speed)

  def move(self, location) : # Unit -> AttackUnit -> FlyableAttackUnit으로 상속되는 move함수를 재정의
    print('[공중 유닛 이동]')
    self.fly(self.name, location)
    
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌쳐', 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
battlecruiser.move('9시')
