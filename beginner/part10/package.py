# 패키지 : 모듈을 모아놓은 집합이라고 생각하면 이해하기 쉽다.
# travel

# import 패키지.모듈 // import 구문에서는 모듈의 클래스나 함수를 직접 불러올 수 없다. from 구문에서는 가능
from travel import vietnam
import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()
