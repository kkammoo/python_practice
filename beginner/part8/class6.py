# pass : 함수 내에서 아무런 동작을 하지 않고 넘어간다는 뜻. 미완성된 함수를 완성된 함수처럼 적용하는 것

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
        pass


# 서플라이 디폿 : 건물, 이 건물 1개당 8유닛 생성
supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')


def game_start():
    print('[알림] 새로운 게임을 시작합니다.')


def game_over():
    pass


game_start()  # 해당 함수 안에 있는 print문 실행
game_over()  # pass로 되어있기 때문에 아무런 동작을 하지 않는다.
