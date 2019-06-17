# 파이썬 프로젝트에 path를 잡았으나 안되는 경우가 있음
# 그냥 sys의 path를 append해서 쓰면됨
import sys
sys.path.append('/cafe24/PycharmProjects/python-modules')
m = __import__('mymath')

print(m.pi)
print(m.add(10, 20))
