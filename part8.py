def sum(a,b):
    result = a+b 
    return result

print(sum(1,2))

def say( ):
    return 'HI'

print(say())

def sum1(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b, a+b))

sum1(1,2)

def say():
    print('Hi')

print(say())


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+ i
    return sum
print(sum_many(1,7,10))


def print_kwarge(**kargs):
    sum = 0
    for k in kargs:
       if(k == "name"):
           print("당신의 이름은 : " + kargs[k])

(print_kwarge(name ="int 조수", b = "2"))

def sum_and_mul(a,b):
    return a+b, a*b, a-b

print(sum_and_mul(1,4))

#값을 박아서 사용
def say_myself(name, old, man = True):
    print("나의 일므은 %s 입니다." % name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("라이라이야",20, False) 
#순서는 맞춰줘야함. 아니면 매핑해야함.

#지역변수
a =1 

def vartest(a):
    a= a+1
vartest(35)
print(a)


b=1
def vartest2(c):
    global b
    b = c+1
    
    #return b => global b로 대체가능

vartest2(32)
print(b)


#람다식
# def add(a,b):
#     return a+b

add = lambda a,b: a+b
myList = [lambda a,b: a+b, lambda a,b: a*b]

print(add(1,3))
print(myList[0](1,2))


a = input("숫자를 입력하세요 : : :")

print(": : : : :" + a)

print("lik" "is" "too" "short")
print("lik" " is" " too" " short") #아래와 동일
print("lik","is","too","short")



