# 사전 (딕셔너리) : Javascript의 객체와 비슷하게 생김
# { key1 : value1, key2 : value2 }
# key값의 경우 중복 불가.

cabinet = {3 : '유재석', 100 : '김태호'}

# value값 불러오기 case 1)
print(cabinet[3]) # Javascript의 객체의 프로퍼티 value값 호출하는 거랑 똑같이 생겼지?
print(cabinet[100])

# print(cabinet[5]) 없는 key값을 불러오면 오류 나고 프로그램 종료

print('==========')

# value값 불러오기 case 2) .get()
print(cabinet.get(3))
print(cabinet.get(100))

print(cabinet.get(5)) # 없는 key값을 불러오면 None 출력
print(cabinet.get(5, '사용가능')) # 두 번째 매개값으로 None 대신 출력할 초기값을 넣어줄 수 있다

print('==========')

# 딕셔너리에 key값이 있는지 확인하기 : key in dictionary // 있으면 True, 없으면 False 반환
print(3 in cabinet)
print(5 in cabinet)

print('==========')

# key값에는 문자열도 올 수 있음.
cabinet = {'A-3' : '유재석', 'A-100' : '김태호'}
print(cabinet)

print('==========')

# 딕셔너리에 새로운 key, value 추가 // dictionary[key] = value
# 만약 key값이 존재하는 값이라면 값이 재할당되기 때문에 주의!
cabinet['C-20'] = '조세호'
print(cabinet)

cabinet['A-3'] = '김종국'
print(cabinet)

print('==========')

# 딕셔너리 값 삭제 : del dictionary[key]
del cabinet['A-3']
print(cabinet)

print('==========')

# 현재 사용중인 key값만 출력 : .keys()
# 현재 사용중인 value값만 출력 : .values()
# key, value 쌍으로 출력 : .items()
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 딕셔너리 전체 삭제 : clear()
cabinet.clear()
print(cabinet)
