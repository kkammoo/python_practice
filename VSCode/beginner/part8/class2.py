# __init__ : 클래스를 통해 객체가 생성될 때 자동으로 불러오는 함수

class Unit :
  def __init__(self, name, hp, damage) :
    self.name = name
    self.hp = hp
    self.damage = damage
    print('{0} 생성되었습니다'.format(self.name))
    print('체력 : {0}, 공격력 : {1}\n'.format(self.hp, self.damage))

marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)


# 멤버 변수 (자바의 멤버 필드)
# 레이스 : 공중 유닛, 비행기, 클로킹이라는 기술을 가지고 있음.
wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage)) # 생성된 객체.멤버 변수로 접근 가능

# 외부에서 멤버 변수를 추가해서 확장할 수 있다 (wraith2를 만들고 clocking 기능 추가)
wraith2 = Unit('신형 레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith2.name, wraith2.damage))
wraith2.clocking = True

if wraith2.clocking == True :
  print('{0}는 현재 클로킹 상태입니다.'.format(wraith2.name))

# print(wraith1.clocking) # wraith2에만 clocking 멤버 변수를 추가했기 때문에 wraith1에서 clocking 멤버 변수를 불러오면 오류가 발생한다.
print(wraith2.clocking)
