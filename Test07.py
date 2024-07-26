class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age

    def say_hello(self, to_name):
        if(self.name == "마이클"):
           print("안녕!" + to_name+" 나는" + self.name + "이야")
        else:
         print("안녕!" + to_name+" 나는" + self.name + "야")

    def introduce(self):
       print("내이름은 "+ self.name + "야 나이는"+ str(self.age))

a = Person("마이클", 20) # p오브젝트를 만듦
b = Person("제니", 21)
c = Person("피오", 33)


a.say_hello("워니야")
b.say_hello("사랑아")
c.say_hello("시리야")

a = Person("워니",30)
a.introduce()

#상속
class Police(Person):
   def arrest(self, to_arrest):
      print("넌 체포되었따. " + to_arrest)

class Programmer(Person):
   def program(self, to_program):
      print("다음에 뭘 만들지? 아 이걸 만들어봐야지? "+ to_program)

wonie = Person("워니", 20)
jenny = Police("제니", 20)
michale = Programmer("마이클", 22)

jenny.introduce()

jenny.arrest("범인")
michale.program("email Program")