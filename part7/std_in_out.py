# 표준 입출력

print('파이썬' + '자바') # +는 문자열 붙이기
print('파이썬', '자바') # ,는 한 칸 공백

# sep : , 공백을 어떻게 표현할 것인지 -> 디폴트는 " "
print('파이썬', '자바', sep = ",")
print('파이썬', '자바', '자바스크립트', sep = " vs ")

# end : 출력문의 끝 부분을 어떻게 처리할 것인지 -> 디폴트는 줄바꿈(\n)
print('파이썬', '자바', sep = ',', end = '?')
print('무엇이 더 재밌을까요?')

# sys모듈 : sys.stdout, sys.stderr
import sys
print('파이썬', '자바', file = sys.stdout) # 표준 출력
print('파이썬', '자바', file = sys.stderr) # 표준 에러 출력 - 일정 시간이 지난 뒤에 출력된다..?

# ljust(공간) : 공간만큼 칸을 확보한 뒤, 왼쪽 정렬
# rjust(공간) : 공간만큼 칸을 확보한 뒤, 오른쪽 정렬
score = {'수학' : 0, '영어' : 50, '코딩' : 100}
for subject, score in score.items() :
  # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")

# 은행 대기순표 001, 002, 003...
for num in range(1, 21) :
  # print("대기번호 : " + str(num)) # 1, 2, 3, 4 ... 21 로 출력
# .zfill(자리수) : 자리수 만큼의 값 중 빈 공간에는 0을 채움
  print("대기번호 : " + str(num).zfill(3)) # 001, 002, 003, 004 ... 021 로 출력

# input의 출력 타입 : 숫자를 입력하든, 문자를 입력하든 input의 출력 타입은 str이다.
answer = input('아무 값을 입력해주세요 (문자, 숫자 노상관)')
print('입력하신 값은 {0}입니다.'.format(answer))
print(type(answer))
