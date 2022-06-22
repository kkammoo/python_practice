# zip 라이브러리

kor = ['사과', '바나나', '오렌지']
eng = ['apple', 'banana', 'orange']

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

print(list(zip(*mixed)))  # zip 해제

kor2, eng2 = zip(*mixed)  # zip해제 후 묶이는 값들을 kor2, eng2 변수에 할당
print(kor2)
print(eng2)
