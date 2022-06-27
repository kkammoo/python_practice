# 예외 처리 : try ~ except (자바의 catch가 파이썬에선 except)
# try문을 실행할 때 에러가 발생하면 except의 타입에 마

try:
    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
except ValueError:  # 틀린 값을 입력했을 때.
    print('잘못된 값을 입력했습니다.')
except ZeroDivisionError as err:  # 숫자를 0으로 나눴을 때
    print(err)
except Exception as err:  # 모든 에러에 관하여 // 어떤 에러인지 특정할 수 없을 때
    print('알 수 없는 에러가 발생하였습니다.')
    print(err)  # 해당 에러가 어떤 에러인지 알 수 있다.
