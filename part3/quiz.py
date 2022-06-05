'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com

규칙 1) http:// 부분은 제외 => naver.com
규칙 2) 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3) 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + '!'로 구성
              (nav)               (5)           (1)            (!)
예) 생성된 비밀번호 : nav51!
'''

# url = 'http://naver.com'
# url = 'http://daum.net'
url = 'http://google.com'

# http:// 제외
password = url.replace('http://', '')

# . 이후 부분 제외
password = password[:password.index('.')]

# 남은 글자 중 처음 세자리
password1 = password[:3]

# 글자 개수
password2 = len(password)

# 글자 내 e 개수
password3 = password.count('e')

# 비밀번호 조합
password = password1 + str(password2) + str(password3) + '!'

# url별 비밀번호 도출
print('{0}의 비밀번호는 {1} 입니다.'.format(url, password))
