#bool 자료형

#a= True
# a = "안녕"
a =""
print(type(a))

if a :
    print(a)

b = [1,2,3,4]
if b :
   print(b)



c = [1,2,3]
#f = c 
f = c[:] #처음부터 끝까지 슬라이싱 해서 복사 == 같은 주소 x 값만 복사
c[1] = 4
print(f)
print(id(c))
print(id(f))
print(f is c )

#a,b = ('python', 'life')
(a,b) = ('python', 'life')
print(a)
print(b)

q = r = 'hello'
print(q)
print(r)

tt = 3
yy = 5
#trr = tt
#tt = yy
# yy = trr 
# 이하 동일 
tt,yy = yy,tt

print(tt)
print(yy)