# 탈출 문자 

# \n : 줄바꿈
print('백문이 불여일견 백견이 불여일타')
print('백문이 불여일견\n백견이 불여일타')

print('==========')

# \"문자\" \'문자\' : 문자열 내 "" 혹은 ''
print('저는 "홍길동" 입니다') # 작은 따옴표로 문자열을 감싸고 큰 따옴표로 강조
print("저는 '홍길동' 입니다") # 큰 따옴표로 문자열을 감싸고 작은 따옴표로 강조

print('==========')

print("저는 \"홍길동\" 입니다") # \"\" 탈출 문자 사용
print('저는 \'홍길동\' 입니다') # \'\' 탈출 문자 사용

print('==========')

# \\ : 문장 내에서 하나의 \
print('d:\javaedu8\python workspace\part3\escape.py')
print('d:\\javaedu8\\python workspace\\part3\\escape.py')

print('==========')

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine') # PineApple 출력

# \b : 백스페이스 (한 글자 삭제)
print('Redd\bApple') # RedApple 출력

# \t : 탭 indent
print('Redd\tApple') # Red  Apple 출력
