# 파일 입출력

# open(파일명, 형식(쓰기 w), 인코딩)
# score_file = open('score.txt', 'w', encoding='utf-8')
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# open(파일명, 형식(추가 a), 인코딩) : .write()
# score_file = open('score.txt', 'a', encoding='utf-8')
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100') # .write는 줄바꿈이 안 되기 때문에 \n 적어줘야 함
# score_file.close()

# 파일 읽기 case 1)
# open(파일명, 형식(읽기 r), 인코딩) : .read()
# score_file = open('score.txt', 'r', encoding='utf-8')
# print(score_file.read()) # score.txt의 모든 내용을 콘솔에 출력
# score_file.close()

# 파일 읽기 case 2)
# open(파일명, 형식(읽기 r), 인코딩) : .readline()
# score_file = open('score.txt', 'r', encoding='utf-8')
# print(score_file.readline()) # score.txt의 내용을 줄별로 읽고, 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 파일 읽기 case 3)
# open(파일명, 형식(읽기 r), 인코딩) : 파일 내용이 몇 문장일지 모를 때 while True: 를 이용해서 출력
# score_file = open('score.txt', 'r', encoding='utf-8')
# while True : 
#   line = score_file.readline()
#   if not line : # 출력할 line이 없으면 break를 통해 while문 빠져나오기
#     break
#   print(line)
# score_file.close()

# 파일 읽기 case 4)
# open(파일명, 형식(읽기 r), 인코딩) : 리스트에 값을 넣어서 출력
score_file = open('score.txt', 'r', encoding='utf-8')
lines = score_file.readlines() # 모든 문장을 list 형태로 저장
for line in lines :
  print(line)
score_file.close()
