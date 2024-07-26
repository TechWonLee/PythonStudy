# tuple
x = ('gdgd',2,3)
y=('a','b','c')

print(x+y)

#tuple과 list 차이는 tuple은 업데이트가 안된다. 튜플은 불변하다.
#x[0] = 10


# 딕셔너리 (key와 value로 이루어져있음) key는 불변값임
x = {"name": "워니",
     "age": 32}

print(x["name"])

print("age" in x)

if "age" in x:
    print("age 는 x 안에 있어요")

print(x.keys())
print(x.values())

for key in x:
    print("key : : : "+str(key))
    print("value : : :"+str(x[key]))


x[0] = "워니"
print(x)

x["school"] = "한빛"
print(x)