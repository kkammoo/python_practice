# __all__
# travel.__init__ 참고


# 모듈 직접 실행 : if __name__ == '__main__' // 모듈 안에서 직접 테스트를 해볼 수 있다

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to2 = thailand.ThailandPackage()
trip_to.detail()
trip_to2.detail()
