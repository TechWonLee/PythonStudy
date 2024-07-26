if 1 > 1:
    print("hello")
elif 2 > 1:  
    print("bye")

def chat(x):
    
    print("안녕하세요 감사해요" + str(x))
chat(2)

def StrChat(name1 , name2, age):
    print(f"{name1}: 안녕? 넌 몇살이니? " )
    print(f"{name2}: 나? 나는 {age} ")

StrChat("이원", "맹기",20)

def dsum(a, b):
    result = a + b
    return result

d = dsum(1, 6)
print(d)

def sayHello(name, age):
    if(age <= 10):
        return print(f"{name}안녕")
    elif(10 < age <= 20):
        return print(f"{name}안녕하세요")
    else: 
        return print(f"{name}안녕하십니까")
    
sayHello("이원", 21)
