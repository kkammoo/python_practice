# 키워드 값 : 매개변수의 값을 지정함으로써 순서에 상관 없이 매개값을 넣을 수 있다.

def profile(name, age, main_lang) :
  print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = '파이썬', age = 25, name = '김태호')
