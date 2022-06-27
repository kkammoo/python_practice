# 문자열 처리 함수

python = 'Python is Amazing'

# lower() : 소문자 출력
print(python.lower())

# upper() : 대문자 출력
print(python.upper())

# isupper() : 대문자인지 확인 (True / False)
print(python[0].isupper())

# len(문자열) : 문자열 길이 반환 (length)
print(len(python))

# replace(a, b) : a 문자열을 b 문자열로 변환
print(python.replace('Python', 'Java'))

# index(value) : 문자열 속 value 문자의 인덱스 번호 추출
# index(value, startIdx) : startIdx부터 시작하는 문자열 속 value 문자의 인덱스 번호 추출
index = python.index('n')
print(index) # Python의 n 인덱스 번호
index = python.index('n', index + 1)
print(index) # Amazing의 n 인덱스 번호

# find(value) : 문자열 속 value 문자의 인덱스 번호 추출. value문자가 없을 경우 -1 반환 // index()는 오류발생
print(python.find('n'))
print(python.find('Java'))

# count(value) : 문자열 속 value 문자가 몇 개 있는지
print(python.count('n'))
