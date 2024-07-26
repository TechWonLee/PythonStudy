##dictionary 키, 벨류로 이루어져 있음. 키는 중복되면 안됨. 벨류는 같아도됨.

a = {1: 'a'}
a['name'] = "익명"
print(a)

b={1 : 'b', 2 : 'c'}
print(b)

print(a.keys())
print(b.values())
print(b.items()) ## 듀플 형태로 쌍으로 담을 수 있음

f= {1: '파랑구름', 2: '손오공', 3:'kking'}
for v in f.values():
    print(v)


#a.clear()

print(1 in a)



