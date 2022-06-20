import pickle

# with : 파일을 다룰 때 with 블록을 통해 명시적으로 close() 메소드를 호출하지 않고도 파일을 닫을 수 있다.
# with open(파일명, 형식, 인코딩) as 파일


# with를 이용한 pickle 읽기
# with open('profile.pickle', 'rb') as profile_file :
#   print(pickle.load(profile_file))


# with를 이용한 파일 쓰기
# with open('study.txt', 'w', encoding='utf-8') as study_file :
#   study_file.write('파이썬을 공부하고 있습니다.')

# with를 이용한 파일 읽기
with open('study.txt', 'r', encoding='utf-8') as study_file :
  print(study_file.read())
