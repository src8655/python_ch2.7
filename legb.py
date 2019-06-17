# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-in

b = 300             # Global
def f():
    b = 200         # Enclosing Function
    def g():
        # b = 100   # Local
        print(b)
        print(__name__)     # Built-in
#                           # 지금은 __main__ 이 나오고
#                           # import해서 f() 호출 시 legb가 나옴
    g()


# __name__ 활용방법
# 아래 f()를 import한 시점에서도 실행되는 문제
# => main에서만 쓰도록 if문에 추가해서 사용
if __name__ == '__main__':
    f()
