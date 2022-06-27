# 가변 인자 : 매개변수를 동적으로 늘리거나 줄이기 *매개변수

def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
  print('이름 : {0}\t나이 : {1}\t'.format(name, age), end = ' ')
  print(lang1, lang2, lang3, lang4, lang5)

profile('유재석', 20, 'python', 'java', 'c', 'c++', 'c#')
profile('김태호', 25, 'kotlin', 'swift', '', '', '')

print('==============')

def profile2(name, age, *language) :
  print('이름 : {0}\t나이 : {1}\t'.format(name, age), end = ' ')
  for lang in language :
    print(lang, end = ' ')
  print()

profile2('유재석', 20, 'python', 'java', 'c', 'c++', 'c#', 'javascript')
profile2('김태호', 25, 'kotlin', 'swift')
