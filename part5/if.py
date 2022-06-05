# if 문

# if 조건 : 
#     실행 명령문
# elif 조건 :
#     실행 명령문
# else :
#     실행 명령문

# 파이썬은 Java와 달리 {} 구분이 없다. 같은 레벨의 실행문은 indent로 구분함

weather = '비'

if weather == '비' :
  print('우산을 챙기세요')
elif weather == '미세먼지' :
  print('마스크를 착용하세요')
else :
  print('준비물 필요 없어요')

# input() : 콘솔에서 값 입력 // Java의 scanner랑 같은 기능
weather = input('오늘 날씨는 어때요? (맑음, 비, 눈, 미세먼지) : ')

if weather == '비' or weather == '눈':
  print('우산을 챙기세요')
elif weather == '미세먼지' :
  print('마스크를 착용하세요')
else :
  print('준비물 필요 없어요')

# 기온 입력 // input은 기본적으로 str 타입. 숫자를 입력해도 int타입으로 적용되지 않기 때문에 int로 형변환 해줘야 한다.
temp = int(input('기온은 어때요? : '))

if temp >= 30 :
  print('너무 더우니 나가지 마세요')
elif 10 <= temp < 30 :
  print('괜찮은 날씨네요')
elif 0 <= temp < 10 :
  print('외투를 챙기세요')
else :
  print('너무 추우니 나가지 마세요')
