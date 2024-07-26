#집합 자료형
#중복허용 x, 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형, 순서없음

#s1 = set([1,2,3])
s1 = {1,2,3}
print(type(s1))

i = [1,2,2,2,2,3,4,4,3,3,10]
newList = list(set(i))
print(newList)

p1 = set("hello")
print(p1)
 

print(s1.intersection(newList))

b1 = set([1,2,3,4,5])
b2 = set([4,5,6,7,8,9])

print(s1 & b1)
print(s1 | b2)
print(s1.union(b2))


