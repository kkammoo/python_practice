# set (집합) : 중복이 안 되고, 순서가 없음

my_set = {1, 2, 3, 3, 3, 4}
print(my_set)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합 : &, .intersection() // java와 python 둘 다 할 수 있는 개발자
print(java & python)
print(java.intersection(python))

print('=============')

# 합집합 : |, .union() // java나 python을 할 수 있는 개발자
print(java | python)
print(java.union(python))

print('=============')

# 차집합 : -, .difference() // java는 할 수 있지만, python은 할 줄 모르는 개발자
print(java - python)
print(java.difference(python))

print('=============')

# python을 할 줄 아는 사람이 늘어남 -> python 집합에 .add로 값 추가
python.add('김태호')
print(python)

print('=============')

# java를 까먹은 김태호 씨 -> java 집합에 .remove()로 값 제거
java.remove('김태호')
print(java)
