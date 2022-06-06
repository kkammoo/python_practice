# 함수의 기본값

def profile(name, age, main_lang) :
  print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'.format(name, age, main_lang))

profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# 같은 학교, 같은 학년, 간은 반, 같은 수업 : 일일이 똑같은 값을 넣어주기 힘들다 -> 이럴 때 기본값 사용
def profile2(name, age=17, main_lang='파이썬') :
  print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'.format(name, age, main_lang))

profile2('유재석') # 나이, 주 사용 언어는 기본값인 17, 파이썬이 출력된다.
profile2('김태호')
