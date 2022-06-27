# 피클(pickle)

import pickle

# pickle 생성 : pickle.dump(데이터, 파일)
# open(파일이름.pickle, wb(b는 바이너리를 의미)) : pickle에서는 인코딩을 안 넣어도 된다.
# profile_file = open('profile.pickle', 'wb')
# profile = {'이름' : '박명수', '나이' : 30, '취미' : ['축구', '골프', '코딩']}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# pickle 읽기 : pickle.load(파일)
# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면, pickle.dump를 사용해서 데이터를 입력한 파일이어야 한다.
profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
