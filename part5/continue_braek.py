# continue & break
# 둘 다 Java에서 적용되던 것과 같은 역할
# continue : 건너뛰고 다음 반복문 실행
# break : 가장 가까운 반복문 탈출

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡함
for student in range(1, 11) :
  if student in absent: 
    continue
  elif student in no_book:
    print('오늘 수업은 여기까지 {0}은 교무실로 따라와!'.format(student))
    break
  print('{0}, 책을 읽어봐'.format(student))
