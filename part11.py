#class

#클래스 쓰는 방법
# 1. class 입력하고 
# 2. 대문자로 시작하는 클래스의 이름을 작성
# 3. 안에 들어갈 함수와 변수 설정


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal2.add(100))

class FourCal:
    pass 

a = FourCal()
print(a)
print(type(a))