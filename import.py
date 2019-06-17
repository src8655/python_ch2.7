# 그냥 import, math를 명시해서 써야함
# import math
# print(math.sin(math.pi/4), math.cos(math.pi/4))

# 특정 함수만 import
# from math import sin, cos, pi
# from mymath import pi           # 같은 이름의 함수가 있다면? => mymath가 덮어버린다
# print(sin(pi/4), cos(pi/4))

# 전부 다 import : 비추
# from math import *
# print(sin(pi/4), cos(pi/4))

# 모듈의 alias(이름)을 지정, 충돌을 막을 수 있다
# import math as m
# from mymath import pi
# print(m.sin(m.pi/4), m.cos(m.pi/4))
# print(pi)

# 모듈이 아닌 함수 이름을 바꾸기
from math import sin as mysin, cos as mycos, pi as mypi
print(mysin(mypi/4), mycos(mypi/4))
