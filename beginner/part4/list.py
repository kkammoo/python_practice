# 리스트 [] : 순서를 가지는 객체의 집합
# Java의 배열을 생각하면 된다. 크기가 동적으로 변하기 때문에 Java보단 Javascript랑 더 비슷할지도..?

subway1 = 10
subway2 = 20
subway3 = 30
subway4 = 40

subway = [10, 20, 30, 40]

print(subway) # 자바의 경우, 배열의 변수를 출력하게 되면 힙 메모리의 스택값이 출력되는데 파이썬은 자바스크립트처럼 배열이 출력된다.

print('==========')

subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호 씨는 몇 번째 칸에 타고 있나?
print(subway.index('조세호'))

print('==========')

# 하하 씨가 다음 정류장에서 탑승하였다 : 배열의 요소 추가 .append() 맨 뒤에 추가
subway.append('하하')
print(subway)

# 정형돈 씨는 유재석 씨와 조세호 씨 사이에 탑승하였다. : 배열의 요소 삽입 insert(index, value) 해당 index 번호 앞에 value값 추가
subway.insert(1, '정형돈')
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하 꺼냄
print(subway) # 하하가 빠진 지하철

print(subway.pop()) # 박명수 꺼냄
print(subway) # 박명수가 빠진 지하철

print(subway.pop()) # 조세호 꺼냄
print(subway) # 조세호가 빠진 지하철

print('==========')

# 같은 이름의 사람이 몇 명 있는지
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

print('==========')

# 리스트 정렬 sort(), reverse()
num_list = [5, 2, 4, 3, 1]
num_list.sort() # sort() : 오름차순 정렬
print(num_list)

num_list.reverse() # 리스트 역순으로 정렬 : sort를 먼저 하고 reverse를 하면 내림차순 정렬이 된다.
print(num_list)

# clear() : 리스트 모두 삭제
num_list.clear()
print(num_list)

print('==========')

# 리스트는 다양한 자료형을 함께 사용할 수 있다
mix_list = ['유재석', 10, '조세호', True]
print(mix_list)

print('==========')

# 리스트 확장 : extend()
num_list = [1, 2, 3, 5]
mix_list = ['유재석', 10, '조세호', True]

num_list.extend(mix_list)
print(num_list) # num_list가 확장되었으므로 num_list를 출력
