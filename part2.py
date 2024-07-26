#튜플 변화를 못함. 바꾸는게 아니라 새로운걸 넣을 순 있음
t1 = (1,2,'a','b')
print(t1[0]) # : :슬라이싱은 됨 , * + 는 됨
t2 = (3,4)
print(t1+t2)

def add(a,b):
    return a+b
