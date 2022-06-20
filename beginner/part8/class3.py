# 메소드 : 클래스 내에 함수(def)로 정의된 동작들
# 상속 : 부모 class의 기능을 물려받기 (자바의 그 상속과 같음) // class 자식 클래스(부모 클래스)

# 일반 유닛
class Unit :
  def __init__(self, name, hp) :
    self.name = name
    self.hp = hp
    # self.damage = damage
    # print('{0} 생성되었습니다'.format(self.name))
    # print('체력 : {0}, 공격력 : {1}\n'.format(self.hp, self.damage))

# 공격 유닛
class AttackUnit(Unit): # AttackUnit class는 Unit class를 상속받았다.
  def __init__(self, name, hp, damage) :
    # self.name = name
    # self.hp = hp
    Unit.__init__(self, name, hp) # Unit class의 __init__ 메소드에서 self.name, self.hp를 가져옴
    self.damage = damage # 자식 class인 AttackUnit class에서 새롭게 추가된 멤버 변수가 됨

  def attack(self, location) : # 메소드의 첫 번째 매개 변수로는 무조건 self를 적어준다 (자바에서 this기능)
    print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

  def damaged(self, damage) :
    print('{0} : {1} 대미지를 입었습니다.'.format(self.name, damage))
    self.hp -= damage
    print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
    if self.hp <= 0 :
      print('{0} : 파괴되었습니다.'.format(self.name))

# 메딕 : 의무병, 공격 유닛이 아님. 아군의 체력 회복 기능

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃', 50, 16)
# 5시로 공격
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
