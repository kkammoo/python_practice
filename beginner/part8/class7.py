# super() : (자바 생성자의 super()와 같은 의미)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(
            self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 대미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))


# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(
            name, location, self.flying_speed))


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # Unit -> AttackUnit -> FlyableAttackUnit으로 상속되는 move함수를 재정의
        print('[공중 유닛 이동]')
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)  # super()를 이용해서 부모 클래스의 정보를 가져올 땐 self를 적지 않는다!
        self.location = location


# 다중 상속에서의 super()
class Person:
    def __init__(self):
        print('Person 생성자')


class Job:
    def __init__(self):
        print('Job 생성자')


class Korean(Person, Job):
    def __init__(self):
        # super().__init__() // 첫 번째 상속 클래스의 __init__() 함수만 출력
        # 다중 상속의 경우, super()가 아닌 각각의 부모클래스의 정보를 가져와야 한다.
        Person.__init__(self)
        Job.__init__(self)


kim = Korean()
