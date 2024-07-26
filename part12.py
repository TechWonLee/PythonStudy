class FourCal:
    def __init__(self, first, second): #init(생성자)쓰면 해당 클래스 작동할때 맨처음 실행해라는 의미임
        self.first = first
        self.second = second
       
    def setdata(self,first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result


a = FourCal(1,2)
#a.setdata(33,22)

print(a.first)
print(a.second)
print(a.add()) 

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.add()) 
print(a.pow())


